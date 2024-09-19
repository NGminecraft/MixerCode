import json
from os import path
import socket


class Config:
    def __init__(self):
        self.local_ip = socket.gethostbyname(socket.gethostname())
        self.local_port = 5005
        self.remote_ip = 192.168.1.1
        self.remote_port = 10024
        self.commands = {
            "gain":"/ch/00/dyn/mgain",
            "fader":"/ch/00/mix/fader"
        }
    

def get_config():
    if path.isfile("settings.json"):
        return json.load("settings.json")
    else:
        return Config()
