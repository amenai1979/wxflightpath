from wxflightpath.wxcrawler import *
from wxflightpath import config
from wxflightpath.audiorender import renderaudio
import uuid
import boto3

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

def createS3BriefiengObject(briefing=["hello","world"],flightpath=["LFPX","LFRU"], expires=3600):
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
    object_key='_'.join(flightpath)+"-"+str(uuid.uuid1())+".txt"
    # Put the object in the S3 bucket
    s3.put_object(Bucket=config['AWS']['BUCKET'], Key=object_key, Body='.'.join(briefing))
    # Construct the URL for the newly created S3 object
    presigned_url = s3.generate_presigned_url('get_object',Params={'Bucket': bucket_name, 'Key': object_key},
        ExpiresIn=expires
    )
    s3_object_url = presigned_url
    return [s3_object_url, bucket_name, object_key]

#configure the secret retrieval
if config["SECURITY"]["TOKEN"] == '':
    secret=get_avwx_secret()
else:
    secret=config["SECURITY"]["TOKEN"]
def getObservationsBriefing (stations=["LFPT"]):
    crawler = Wxcrawler(config=config, secret=secret)
    logging.info("initiated Observation wxcrawler")
    observationsBriefing=[]
    if stations:
        for station in stations:
            try:
                rawObservation = crawler.getObservationWX(station)
                observationsBriefing.append(crawler.formatObservationWX(rawObservation))
            except Exception as e:
                logging.exception("error generation observation briefing for %s, full error:", station, e)
                pass
    logging.info("Observations briefing generated")
    return observationsBriefing
def threadedGetObservationsBriefing (stations=["LFPT"]):
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
    [observationsBriefing.append(crawler.formatObservationWX(ro[1])) for ro in crawler.orderObsResults(desired_order=airfields)]
    logging.info("Observations briefing generated")
    return observationsBriefing

def getForecastBriefing (stations=["LFPG"]):
    crawler = Wxcrawler(config=config, secret=secret)
    logging.info("initiated Forecast wxcrawler")
    forecastBriefing=[]
    if stations:
        for station in stations:
            try:
                rawForecast = crawler.getForecastWX(station)
                forecastBriefing.append(crawler.formatForecastWX(rawForecast))
            except Exception as e:
                logging.exception("error generation forcast briefing for %s, full error:", station, e)
                pass
    logging.info("Forecast briefing generated")
    return forecastBriefing
def threadedGetForecastBriefing (stations=["LFPG"]):
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
    [ForecastBriefing.append(crawler.formatForecastWX(rf[1])) for rf in crawler.orderForResults(desired_order=airfields)]
    logging.info("Forecasts briefing generated")
    return ForecastBriefing
def lambda_handler(event, context):
    #Create the briefing
    #1 - get airfields on the flight path
    if 'flightpath' not in event.keys():
        event["flightpath"]=["LFPX","LFRU"]
    flightpath=event["flightpath"]
    stations=getAirfieldsInFlightPath(flightpath[0], flightpath[1])
    assert len(stations)>=1
    #2 - Create the briefing
    briefing=[]
    observations = getObservationsBriefing(stations)
    forecasts = getForecastBriefing(stations)
    briefing.append(" Here are the latest observations for your flight path from "+sayInternational(input=flightpath[0]) + " to " + sayInternational(input=flightpath[1]))
    briefing += observations + ["\n"]
    briefing.append(" Here are the latest forecasts for your flight path from "+sayInternational(input=flightpath[0]) + " to " + sayInternational(input=flightpath[1]))
    briefing+=forecasts
    logging.info("briefing generated")
    logging.info(briefing)
    # 3 - generate the s3 object and log the URL
    object_data= createS3BriefiengObject(briefing,flightpath)
    logging.info("uploaded briefing to s3")
    s3_object_url=object_data[0]
    logging.info(s3_object_url)
    #4 respond to the caller
    response = {
            'statusCode': 200,
            'headers': {
                'BriefingURL': s3_object_url
            },
            'body': ".".join(briefing)
    }
    return response
def faster_lambda_handler(event, context):
    #Create the briefing
    #1 - get airfields on the flight path
    if 'flightpath' not in event.keys():
        event["flightpath"]=["LFPX","LFRU"]
    flightpath=event["flightpath"]
    stations=getAirfieldsInFlightPath(flightpath[0], flightpath[1])
    assert len(stations)>=1
    #2 - Create the briefing
    briefing=[]
    observations = threadedGetObservationsBriefing(stations)
    forecasts = threadedGetForecastBriefing(stations)
    briefing.append(" Here are the latest observations for your flight path from " + sayInternational(
        input=flightpath[0]) + " to " + sayInternational(input=flightpath[1]))
    briefing += observations + ["\n"]
    briefing.append(" Here are the latest forecasts for your flight path from " + sayInternational(
        input=flightpath[0]) + " to " + sayInternational(input=flightpath[1]))
    briefing+=forecasts
    logging.info("briefing generated")
    logging.info(briefing)
    # 3 - generate the s3 object and log the URL
    object_data= createS3BriefiengObject(briefing,flightpath)
    logging.info("uploaded briefing to s3")
    s3_object_url=object_data[0]
    logging.info(s3_object_url)
    #4 respond to the caller
    response = {
            'statusCode': 200,
            'headers': {
                'BriefingURL': s3_object_url
            },
            'body': ".".join(briefing)
    }
    return response
def demo_aws():
    event = {'flightpath': ["LFRU", "LFPT"]}
    logging.info("Thank you for choosing wxflightpath!")
    #logging.info("comparing performance improvements before and after multithreading introduction")
    #logging.info("without multithreading start")
    #briefing = lambda_handler(event, {})
    #logging.info("without multithreading end")
    #logging.info("with multithreading start")
    briefing = faster_lambda_handler(event, {})
    #logging.info("with multithreading end")
    #renderaudio(input=briefing['body'])
if __name__=='__main__':
    demo_aws()


