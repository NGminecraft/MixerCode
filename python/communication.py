import logging
from utilClasses.cmd import CMD
import socket
from pythonosc import dispatcher
from pythonosc import osc_server, udp_client
import asyncio
from config import Config

class Comms:
    def __init__(self, config:Config):
        self.logger = logging.getLogger("logger.main")
        # This checks the config to check for the local devices ip and port for 
        # This is for the part of the server responsible for receiving data (local devices data)
        self.mainDispatcher = dispatcher.Dispatcher()
        self.server = osc_server.AsyncIOOSCUDPServer((config.local_ip, config.local_port), self.mainDispatcher, asyncio.get_event_loop())
        self.logger.info(f"Starting server on {config.local_ip}:{config.local_port}")
        self.server.serve()
        self.logger.info("Started server, setting up client side")
        # This is setting up the sending of data (mixers data)
        self.client = udp_client.SimpleUDPClient(config.remote_ip, config.remote_port)
        # Even though you technically sholdn't do this, I'm desperate
        self.client._sock.bind((config.local_ip, config.local_port))
    
    def registerListener(self, func_object, cmd:CMD):
        if cmd:
            self.logger.debug(f"Added listener to {cmd}")
            self.mainDispatcher.map(str(CMD), func_object)
        else:
            self.logger.error(f"The command {cmd} is not registered as an input")
            
    def sendMessage(self, cmd, value=None):
        self.logger.debug(f"Sending message of {cmd} with value {value}")
        self.client.send_message(cmd, value)
            
