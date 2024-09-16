keyboard = True
try:
    from pynput.keyboard import Key, Listener, Controller
except ImportError:
    keyboard = False
from multiprocessing import process
import logging
from utilClasses.cmd import CMD

class KeyLogger:
    def __init__(self, register_cmd_function):
        if not keyboard:
            self.logger = logging.getLogger("logger.main")
            self.logger.error("Envrionment errors, unable to start keylogger")
            self.logger.error("Check that your running on a standard windows machine")
            return None
        else:
            self.logger = logging.getLogger("logger.main")
            self.logger.info("Starting the keylogger")
            #--CONSTANTS--
            _space_func = lambda : setattr(self, 'typed_string', self.typed_string + " ")
            _backspace_func = lambda : setattr(self, 'typed_string', self.typed_string[0:-1])
            #--CONSTANTS--
            self.keys = {Key.esc: self.stop,
                         Key.space: _space_func,
                         Key.backspace: _backspace_func}
            self.listener = self.start()
        
            self.typed_string = ""
            
            self.handler_register = register_cmd_function
            



    def start(self):
        self.controller = Controller()
        listener = Listener(on_press = self._on_press, on_release = self._on_release, suppress=True)
        listener.start()
        return listener
        
    def _on_press(self, key):
        self.logger.debug(f"{self.typed_string}")
        if key in self.keys.keys():
            self.keys[key]()
        else:
            with self.controller.modifiers as modifiers:
                if len(modifiers) > 0:
                    # Insert non-typing code here
                    return
            try:
                self.logger.debug(f"Recieved keypress of {key}")
                self.typed_string += key.char
            except AttributeError:
                if key == Key.enter:
                    self.decode_command(self.typed_string)
                    self.typed_string = ""
            
    
    def _on_release(self, key):
        pass
    
    def register_key(self, key, functionObject):
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append(functionObject)
    
    def stop(self):
        self.logger.info("Shutting down KeyLogger")
        self.listener.stop()
        # Right here add the methods to stop the rest of the code
        
    def decode_command(self, string):
        string = string.split(" ")
        if string[0] == "track":
            self.logger.debug(f"started tracking {string[1:]}")
            self.handler_register(*string[1:])
            