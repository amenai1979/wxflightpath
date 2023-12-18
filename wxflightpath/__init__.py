import os
import sys
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

