keyboard = True
try:
    from pynput.keyboard import Key, Listener
except ImportError:
    keyboard = False
from multiprocessing import process
import logging
import asyncio

class KeyLogger:
    async def __init__(self):
        if not keyboard:
            self.logger = logging.getLogger("logger.main")
            self.logger.error("Envrionment errors, unable to start keylogger")
            self.logger.error("Check that your running on a standard windows machine")
            return None
        else:
            self.stopping = False
            self.logger = logging.getLogger("logger.main")
            self.logger.info("Starting the keylogger")
            self.keys = {Key.esc: [self.stop]}
        
            with Listener(on_press = self._on_press, on_release = self._on_release, suppress=True) as listener:
                listener.join()
        
    def _on_press(self, key):
        if self.stopping:
            return False
        elif key in self.keys.keys():
            self.keys[key]()
        else:
            print(key)
    
    def _on_release(self, key):
        if self.stopping:
            return False
    
    def register_key(self, key, functionObject):
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append(functionObject)
    
    def stop(self):
        self.logger.info("Shutting down KeyLogger")
        self.stopping = True
        # Right here add the methods to stop the rest of the code
    
    