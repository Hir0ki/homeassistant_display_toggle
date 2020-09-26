import logging
from pathlib import Path
import configparser
import sys


class Config:

    def __init__(self, config_path: str):
        logging.info(f"Config Path: {config_path}")
        config_path = Path(config_path)
        if config_path.is_file and config_path.exists():
            self.config = configparser.ConfigParser()
            self.config.read(config_path)
        else: 
            logging.error("Didn't find config file")
            sys.exit(1)
        

    def get_password(self):
        return self.config['MQTT']['password'] 
    
    def get_username(self):
        return self.config['MQTT']['username'] 

    def get_url(self):
        return self.config['MQTT']['url'] 
        
    def get_port(self):
        return int(self.config['MQTT']['port'])
    
    def get_device_name(self):
        return  self.config['DEVICE']['name']