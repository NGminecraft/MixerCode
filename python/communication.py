import logging
from utilClasses.cmd import CMD
<<<<<<< HEAD
=======
import socket
>>>>>>> c4d2f088005f40a683c0538e6f513bd420849fa7
from pythonosc import dispatcher
from pythonosc import osc_server, udp_client
import asyncio
from config import Config
<<<<<<< HEAD
import socket
import asyncio

=======
>>>>>>> c4d2f088005f40a683c0538e6f513bd420849fa7

class Comms:
    def __init__(self, config:Config):
        self.logger = logging.getLogger("logger.main")
<<<<<<< HEAD
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((config.local_ip, config.local_port))
        self.socket.setblocking(False)
        # Setting the socket as the asyncio datagram socket
        # This is for the part of the server responsible for receiving data (local devices data)
        self.mainDispatcher = dispatcher.Dispatcher()
        self.server = osc_server.AsyncIOOSCUDPServer((config.local_ip, 5843), self.mainDispatcher, asyncio.get_event_loop())
        
        async def create_server():
            transport, protocol = await asyncio.get_event_loop().create_datagram_endpoint(
                lambda: self.server._OSCProtocolFactory(self.mainDispatcher),
                sock=self.socket
            )
            return transport, protocol
        self.logger.info(f"Starting server on {config.local_ip}:{config.local_port}, ({self.server.socket.getsockname()})")
        
        self.logger.info("Started server, setting up client side")
        # This is setting up the sending of data (mixers data)
        self.client = udp_client.SimpleUDPClient(config.remote_ip, config.remote_port)
        # Even though you technically shouldn't do this, I'm desperate
        self.client._sock = self.socket
        self.logger.info(f"Set up client server on {self.client._sock.getsockname()}")
        # asyncio get event loop run until ocmplete(create_server())
        # loop.run_forever()
        
=======
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
>>>>>>> c4d2f088005f40a683c0538e6f513bd420849fa7
    
    def registerListener(self, func_object, cmd:CMD):
        if cmd:
            self.logger.debug(f"Added listener to {cmd}")
            self.mainDispatcher.map(str(CMD), func_object)
        else:
            self.logger.error(f"The command {cmd} is not registered as an input")
            
    def sendMessage(self, cmd, value=None):
        self.logger.debug(f"Sending message of {cmd} with value {value}")
        self.client.send_message(cmd, value)
            
<<<<<<< HEAD
"""
This I think is the type of socket we need to make
    shared_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    shared_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    shared_socket.bind((local_ip, port))  # Bind to the local address and port
    shared_socket.setblocking(False)  # Set non-blocking mode
    
We need to set the socket used in client._sock as well as the one in self.server.socket to this (hopefully)
"""
=======
>>>>>>> c4d2f088005f40a683c0538e6f513bd420849fa7
