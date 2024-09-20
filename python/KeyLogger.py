from CommandHandler import CommandHandler
keyboard = True
try:
    from pynput.keyboard import Key, Listener, Controller
except ImportError:
    keyboard = False
import logging  # noqa: E402

class KeyLogger:
    def __init__(self, register_cmd_function, send_cmd_function, cmdClass:CommandHandler):
        if not keyboard:
            self.logger = logging.getLogger("logger.main")
            self.logger.error("Environment errors, unable to start keylogger")
            self.logger.error("Check that your running on a standard windows machine")
            return None
        else:
            self.logger = logging.getLogger("logger.main")
            self.logger.info("Starting the keylogger")
            
            self.cmdClass = cmdClass
            
            #--CONSTANTS--
            def _space_func():
                return setattr(self, "typed_string", self.typed_string + " ")
            def _backspace_func():
                return setattr(self, "typed_string", self.typed_string[0:-1])
            #--CONSTANTS--
            self.keys = {Key.esc: self.stop,
                         Key.space: _space_func,
                         Key.backspace: _backspace_func}
            self.listener = self.start()
        
            self.typed_string = ""
            
            self.handler_register = register_cmd_function
            self.send_message = send_cmd_function
            



    def start(self):
        self.controller = Controller()
        listener = Listener(on_press = self._on_press, on_release = self._on_release, suppress=True)
        listener.start()
        return listener
        
    def _on_press(self, key):
        if key in self.keys.keys():
            self.keys[key]()
        else:
            with self.controller.modifiers as modifiers:
                if len(modifiers) > 0:
                    # Insert non-typing code here
                    return
            try:
                self.typed_string += key.char
            except AttributeError:
                if key == Key.enter:
                    print("\033[?1049l")
                    self.logger.debug(f"Process command {self.typed_string}")
                    self.cmdClass.process_command(self.typed_string)
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
        elif string[0] == "send":
            self.logger.debug(f"sending command: {string[1:]}")
            self.send_message(*string[1:])