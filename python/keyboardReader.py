from pynput.keyboard import Key, Listener
from multiprocessing import process
import logging


class KeyLogger:
    def __init__(self):
        self.stopping = False
        self.logger = logging.getLogger("logger.main")
        self.logger.info("Starting the keylogger")
        self.keys = {Key.esc: [self.stopKeylogging]}
        
        with Listener(on_press = self._on_press, on_release = self._on_release, suppress=True) as listener:
            listener.join()
        
    def _on_press(self, key):
        if self.stopping:
            return False
        elif key in self.keys.keys():
            self.keys[key]()
    
    def _on_release(self, key):
        if self.stopping:
            return False
    
    def register_key(self, key:Key, functionObject):
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append(functionObject)
    
    def stop(self):
        self.stopping = True
        # Right here add the methods to stop the rest of the code
    
    