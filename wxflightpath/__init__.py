import os
import sys
import boto3
from botocore.exceptions import ClientError
import json
current_path=os.getcwd()
sys.path.append(current_path)
parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
sys.path.append(parent_path)
#some initializations
import logging
from configparser import *

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # Output logs to the console
    ]
)
#Load the config file.
configfile = '../default.cfg' #replace with the correct config file if needed
config = ConfigParser()
config.read(configfile)
logging.info("loaded config file: %s", configfile)
#get the AWS secret for secrets manager
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
    except ClientError as e:
        logging.exception("Error: %s", e)
    # return avwx apikey if everything goes as expected.
    return apikey['avwxapikey']
awssecret=get_avwx_secret()