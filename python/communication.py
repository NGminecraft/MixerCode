import logging
from utilClasses.cmd import CMD
import socket
from pythonosc import dispatcher
from pythonosc import osc_server, udp_client, osc_message_builder
import socket
import asyncio

class Comms:
    def __init__(self):
        self.logger = logging.getLogger("logger.main")
        # This checks the config to check for the local devices ip and port for 
        try:
            # looks for IP in the config file
            with open("config.config", "r") as file:
                lines = [i.rstrip("\n").split(":")[-1] for i in file.readlines()]
            self.logger.info(f"Found config.config and got the data {lines}")
            ip = lines[0]
            port = int(lines[1])
            local_port = lines[2]
        except FileNotFoundError|IndexError:
            # Asks for ip if config doesn't exist or is wrong
            ip = input("Enter the IP: ")
            port = input("Enter the port: ")
            local_port = 5005
        # This is for the part of the server responsible for receiving data (local devices data)
        self.mainDispatcher = dispatcher.Dispatcher()
        self.server = osc_server.AsyncIOOSCUDPServer((str(socket.gethostbyname(socket.gethostname())), local_port), self.mainDispatcher, asyncio.get_event_loop())
        self.logger.info(f"Starting server on {str(socket.gethostbyname(socket.gethostname()))}:{local_port}")
        self.server.serve()
        self.logger.info(f"Started server, setting up client side")
        try:
            # Creates a socket for a specific port
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.bind(('', local_port))
            # This is setting up the sending of data (mixers data)
            self.client = udp_client.SimpleUDPClient(ip, int(port), sock=self.sock)
        except TypeError:
            self.logger.critical("INVALID INPUT RECEIVED, QUITTING")
            quit("Ending")
    
    def registerListener(self, func_object, cmd:CMD):
        if cmd:
            self.logger.debug(f"Added listener to {cmd}")
            self.mainDispatcher.map(str(CMD), func_object)
        else:
            self.logger.error(f"The command {cmd} is not registered as an input")
            
    def sendMessage(self, cmd, value=None):
        self.logger.debug(f"Sending message of {cmd} with value {value}")
        self.client.send_message(cmd, value)
            