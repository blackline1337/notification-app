from typing import Union
import os
import configparser
from datetime import datetime
from fastapi import FastAPI
from generate import generate_config

app = FastAPI()

def load_configuration(config_file='secretkeys.conf'):
    # Load config file
    config = configparser.ConfigParser()
    if os.path.exists(config_file):
        return {
            'secret_path': config['secrets']['api_path'],
            'api_key': config['secrets']['api_key']
            }
    raise FileNotFoundError(f"Configuration file {config_file} not found")

config_data = generate_config()
print(f"Generated URL for admin: http://localhost/{config_data['api_path']}")
secret_path = config_data['api_path']
api_key = config_data['api_key']


@app.get("/")
def read_root():
    return {"Notifications": "App"}


@app.get("/notifications")
def read_notifications():
    messages = "test"
    # access the mysql database to read available notifications and output in json
    return messages

@app.post("/{secret_path}")
def add_notifications():
    # if the api_key value matches to configuration file api key, submit the message to the database.
    # ensure secret_key matches before adding the message to the database
    # access the mysql database to add notifications
    return "sucess"