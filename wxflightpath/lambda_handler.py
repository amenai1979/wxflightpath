import os
import uuid

import boto3

from wxflightpath import config
from wxflightpath.audiorender import renderaudio
from wxflightpath.wxcrawler import *
from wxflightpath.zoneFilter import validateAirfield


def get_avwx_secret():
    try:
        secret_name = config['AWS']['SECRET_NAME']
        assert secret_name != ''
        region_name = config['AWS']['REGION_NAME']
        assert region_name != ''
    except AssertionError as a:
        logging.error("You may have not configured the AWS section of default.cfg properly.")
        raise
    # Create a Secrets Manager client
    try:
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )
        logging.info("initiated secretsmanager client: %s", client)
    except Exception as e:
        logging.exception("Error: %s", e)
    # Grab the api secret key
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        apikey = json.loads(get_secret_value_response['SecretString'])
        logging.info("secret retrieved")
    except Exception as e:
        logging.exception("Error: %s", e)
    # return avwx apikey if everything goes as expected.
    return apikey['avwxapikey']


def createS3BriefiengObject(briefing=["hello", "world"], flightpath=["LFPX", "LFRU"], expires=86400):
    try:
        bucket_name = config['AWS']['BUCKET']
        assert bucket_name != ''
    except AssertionError as a:
        logging.error("You have not configured the AWS section of default.cfg properly.")
        raise
    # initiate an s3 client
    try:
        s3 = boto3.client('s3')
        logging.info("initiated s3 client: %s", s3)
    except Exception as e:
        logging.exception("Error: %s", e)
    object_key = '_'.join(flightpath) + "-" + str(uuid.uuid1()) + ".txt"
    # Put the object in the S3 bucket
    s3.put_object(Bucket=config['AWS']['BUCKET'], Key=object_key, Body='.'.join(briefing))
    # Construct the URL for the newly created S3 object
    presigned_url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': object_key},
                                              ExpiresIn=expires
                                              )
    s3_object_url = presigned_url
    return [s3_object_url, bucket_name, object_key]


def createS3AudioBriefiengObject(audio="filename.mp3", flightpath=["LFPX", "LFRU"], expires=86400):
    try:
        bucket_name = config['AWS']['BUCKET']
        assert bucket_name != ''
    except AssertionError as a:
        logging.error("You have not configured the AWS section of default.cfg properly.")
        raise
    # initiate an s3 client
    try:
        s3 = boto3.client('s3')
        logging.info("initiated s3 client: %s", s3)
    except Exception as e:
        logging.exception("Error: %s", e)
    object_key = '_'.join(flightpath) + "-" + str(uuid.uuid1()) + ".mp3"
    # Put the object in the S3 bucket
    s3.upload_file(Key=object_key, Bucket=config['AWS']['BUCKET'], Filename=audio)
    # Construct the URL for the newly created S3 object
    presigned_url = s3.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': object_key},
                                              ExpiresIn=expires
                                              )
    s3_object_url = presigned_url
    return [s3_object_url, bucket_name, object_key]


# configure the secret retrieval
if config["SECURITY"]["TOKEN"] == '':
    secret = get_avwx_secret()
else:
    secret = config["SECURITY"]["TOKEN"]


def getObservationsBriefing(stations=["LFPT"], lang="en"):
    crawler = Wxcrawler(config=config, secret=secret)
    logging.info("initiated Observation wxcrawler")
    observationsBriefing = []
    if stations:
        for station in stations:
            try:
                rawObservation = crawler.getObservationWX(station)
                observationsBriefing.append(crawler.formatObservationWX(rawObservation, lang = lang))
            except Exception as e:
                logging.exception("error generation observation briefing for %s, full error:", station, e)
                pass
    logging.info("Observations briefing generated")
    return observationsBriefing


def threadedGetObservationsBriefing(stations=["LFPT"],lang="en"):
    observationsBriefing = []
    crawler = Wxcrawler(config=config, secret=secret)
    logging.info("initiated Observation wxcrawler")
    startTime = time.time()
    logging.info("observations collection has started at %i", startTime)
    airfields = stations
    # start threads to get observation weather for each airfield
    [threading.Thread(target=crawler.threadGetObservationWX, args=(airfield,)).start() for airfield in airfields]
    # join all threads
    [thread.join() for thread in threading.enumerate() if thread != threading.current_thread()]
    endTime = time.time()
    logging.info("observations collection has completed in %i seconds", endTime - startTime)
    [observationsBriefing.append(crawler.formatObservationWX(ro[1],lang=lang)+ "\n") for ro in
     crawler.orderObsResults(desired_order=airfields)]
    logging.info("Observations briefing generated")
    return observationsBriefing


def getForecastBriefing(stations=["LFPG"], lang = "en"):
    crawler = Wxcrawler(config=config, secret=secret)
    logging.info("initiated Forecast wxcrawler")
    forecastBriefing = []
    if stations:
        for station in stations:
            try:
                rawForecast = crawler.getForecastWX(station)
                forecastBriefing.append(crawler.formatForecastWX(rawForecast, lang=lang))
            except Exception as e:
                logging.exception("error generation forecast briefing for %s, full error:", station, e)
                pass
    logging.info("Forecast briefing generated")
    return forecastBriefing


def threadedGetForecastBriefing(stations=["LFPG"], lang = "en"):
    ForecastBriefing = []
    crawler = Wxcrawler(config=config, secret=secret)
    logging.info("initiated Forecast wxcrawler")
    startTime = time.time()
    logging.info("Forecasts collection has started at %i", startTime)
    airfields = stations
    # start threads to get observation weather for each airfield
    [threading.Thread(target=crawler.threadGetForecastWX, args=(airfield,)).start() for airfield in airfields]
    # join all threads
    [thread.join() for thread in threading.enumerate() if thread != threading.current_thread()]
    endTime = time.time()
    logging.info("Forecasts collection has completed in %i seconds", endTime - startTime)
    [ForecastBriefing.append(crawler.formatForecastWX(rf[1], lang = lang) + "\n") for rf in
     crawler.orderForResults(desired_order=airfields)]
    logging.info("Forecasts briefing generated")
    return ForecastBriefing


def lambda_handler(event, context):
    # Create the briefing
    #
    lang = "en"
    # 1 - get airfields on the flight path
    if 'flightpath' not in event.keys():
        event["flightpath"] = ["LFPX", "LFRU"]
    flightpath = event["flightpath"]
    stations = getAirfieldsInFlightPath(flightpath[0], flightpath[1])
    assert len(stations) >= 1
    # 2 - Create the briefing
    briefing = []
    observations = getObservationsBriefing(stations)
    forecasts = getForecastBriefing(stations)
    if lang != "fr":
      briefing.append("Information in this briefing may be inaccurate and incomplete. it does not replace thorough flight planning. You are required to rely on official sources of information only when making aeronautical decisions. Here are the latest observations for your flight path from " + sayInternational(
        input=flightpath[0]) + " to " + sayInternational(input=flightpath[1]))
      briefing += observations + ["\n"]
      briefing.append("Information in this briefing may be inaccurate and incomplete. it does not replace thorough flight planning. You are required to rely on official sources of information only when making aeronautical decisions. Here are the latest forecasts for your flight path from " + sayInternational(
        input=flightpath[0]) + " to " + sayInternational(input=flightpath[1]))
      briefing += forecasts
    logging.info("briefing generated")
    logging.info(briefing)
    # 3 - generate the s3 object and log the URL
    object_data = createS3BriefiengObject(briefing, flightpath)
    logging.info("uploaded briefing to s3")
    s3_object_url = object_data[0]
    logging.info(s3_object_url)
    # 4 respond to the caller
    response = {
        'statusCode': 200,
        'headers': {
            'BriefingURL': s3_object_url
        },
        'body': ".".join(briefing)
    }
    return response


def faster_lambda_handler(event, context):
    # Create the briefing
    # 0- assume default language english
    lang = "en"
    # 1 - get airfields on the flight path
    if "flightpath" in event["queryStringParameters"].keys():
        flightpath = event["queryStringParameters"]["flightpath"]
        flightpath = flightpath.split(',')
        assert len(flightpath) > 1
        assert [validateAirfield(x) for x in flightpath]
        logging.info("successfully extracted flightpath origin %s and destination %s", flightpath[0], flightpath[1])
    else:
        logging.error("unable to extract flightpath from request")
        response = {
            'statusCode': 400,
            'body': '<b>Invalid request query param try a request with the following query parameter pattern /?flightpath=LFRO,LFPX</b>'
        }
        return response
    # check if translation is needed
    if "translate" in event["queryStringParameters"].keys():
        lang = event["queryStringParameters"]["translate"]
    #generate the forecast
    stations = getAirfieldsInFlightPath(flightpath[0], flightpath[1])
    assert len(stations) >= 1
    # 2 - Create the briefing
    briefing = []
    observations = threadedGetObservationsBriefing(stations,lang=lang)
    forecasts = threadedGetForecastBriefing(stations, lang = lang)
    if lang != "fr":
        briefing.append("Information in this briefing may be inaccurate and incomplete. it does not replace thorough flight planning. You are required to rely on official sources of information only when making aeronautical decisions.\nHere are the latest observations for your flight path from " + sayInternational(
            input=flightpath[0]) + " to " + sayInternational(input=flightpath[1]) + "\n")
        briefing += observations + ["\n"]
        briefing.append("Information in this briefing may be inaccurate and incomplete. it does not replace thorough flight planning. You are required to rely on official sources of information only when making aeronautical decisions.\nHere are the latest forecasts for your flight path from " + sayInternational(
            input=flightpath[0]) + " to " + sayInternational(input=flightpath[1]) + "\n")
        briefing += forecasts + ["\n"]
    else:
        briefing.append("Les informations ci-après peuvent être incomplètes et contenir des erreurs. Elles ne remplacent pas une préparation complète de votre vol. Vous devez vous appuyez uniquement sur des sources officielles pour la prise de décisions aéronautiques.\nCi-après les observations météorologiques pour votre vol de " + sayInternational(
            input=flightpath[0]) + " à  " + sayInternational(input=flightpath[1]) + "\n")
        briefing += observations + ["\n"]
        briefing.append("Les informations ci-après peuvent être incomplètes et contenir des erreurs. Elles ne remplacent pas une préparation complète de votre vol. Vous devez vous appuyez uniquement sur des sources officielles pour la prise de décisions aéronautiques.\nCi-après les prévisions météorologiques pour votre vol de " + sayInternational(
            input=flightpath[0]) + " à " + sayInternational(input=flightpath[1]) + "\n" )
        briefing += forecasts + ["\n"]
    logging.info("briefing generated for flightpath origin %s and destination %s", flightpath[0], flightpath[1])
    # logging.info(briefing)
    # 3 - generate the s3 object and log the URL
    if "audio" in event["queryStringParameters"].keys():
        filename = renderaudio(input=".".join(briefing), title=str(uuid.uuid4()))
        object_data = createS3AudioBriefiengObject(audio=filename, flightpath=flightpath)
        # clean up the audio file from persistent local storage
        if os.path.exists(filename):
            os.remove(filename)
        s3_object_url = object_data[0]
        logging.info("uploaded audio briefing for flightpath origin %s and destination %s to s3", flightpath[0],
                     flightpath[1])
        logging.info("Audio briefing available here %s: ", s3_object_url)


    # 4 respond to the caller
    else:
        object_data = createS3BriefiengObject(briefing, flightpath)
        logging.info("uploaded briefing to s3")
        s3_object_url = object_data[0]
        print(s3_object_url)

    response = {
        'statusCode': 200,
        'headers': {
            'Location': s3_object_url
        },
        'body': s3_object_url
    }
    return response


def demo_aws():
    event = {
        "version": "2.0",
        "routeKey": "$default",
        "rawPath": "/path/to/resource",
        "rawQueryString": "flightpath=LFPX,LFRU",
        "cookies": [
            "cookie1",
            "cookie2"
        ],
        "headers": {
            "Header1": "value1",
            "Header2": "value1,value2"
        },
        "queryStringParameters": {
            "flightpath": 'LFRO,LFRO',
            #"audio": None,
            "translate" : "fr"
        },
        "requestContext": {
            "accountId": "123456789012",
            "apiId": "api-id",
            "authentication": {
                "clientCert": {
                    "clientCertPem": "CERT_CONTENT",
                    "subjectDN": "www.example.com",
                    "issuerDN": "Example issuer",
                    "serialNumber": "a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1:a1",
                    "validity": {
                        "notBefore": "May 28 12:30:02 2019 GMT",
                        "notAfter": "Aug  5 09:36:04 2021 GMT"
                    }
                }
            },
            "authorizer": {
                "jwt": {
                    "claims": {
                        "claim1": "value1",
                        "claim2": "value2"
                    },
                    "scopes": [
                        "scope1",
                        "scope2"
                    ]
                }
            },
            "domainName": "id.execute-api.us-east-1.amazonaws.com",
            "domainPrefix": "id",
            "http": {
                "method": "POST",
                "path": "/path/to/resource",
                "protocol": "HTTP/1.1",
                "sourceIp": "192.168.0.1/32",
                "userAgent": "agent"
            },
            "requestId": "id",
            "routeKey": "$default",
            "stage": "$default",
            "time": "12/Mar/2020:19:03:58 +0000",
            "timeEpoch": 1583348638390
        },
        "body": [
            "LFRO",
            "LFRU"
        ],
        "pathParameters": {
            "parameter1": "value1"
        },
        "isBase64Encoded": True,
        "stageVariables": {
            "stageVariable1": "value1",
            "stageVariable2": "value2"
        }
    }
    logging.info("Thank you for choosing wxflightpath!")
    faster_lambda_handler(event, context={})


if __name__ == '__main__':
    demo_aws()
