from logging.config import dictConfig
from .config import Config
import os
import logging
import yaml
import pathlib

#Add new config parameter her
CONFIG_PATH = os.getenv("CONFIG_PATH", "./config.ini")
#Path to the logging config file in a yml format
LOG_CONFIG_PATH = os.getenv("LOG_CONFIG_PATH", "./logging.yml")
#Log Level for the root logger 
LOG_LEVEL_ROOT = os.getenv("LOG_LEVEL_ROOT", "INFO")
#Log level for the Project root logger 
LOG_LEVEL_HOMEASSISTANT_DISPLAY_TOGGLE = os.getenv("LOG_LEVEL_HOMEASSISTANT_DISPLAY_TOGGLE", "INFO")


#Load yml logging config
logging_config_path = pathlib.Path(LOG_CONFIG_PATH)
logging.info(f"Logging cofng path is {LOG_CONFIG_PATH}")
if logging_config_path.is_file():
    with open(logging_config_path, "rt") as file:
        logging_config = yaml.safe_load(file.read())
else:
    logging.error("Couldn't find the logging config", exc_info=True)
    raise ValueError("Error while loading logging config")

dictConfig(logging_config)

CONFIG: Config = Config(CONFIG_PATH)