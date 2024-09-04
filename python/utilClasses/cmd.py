import logging


class CMD:
    def __init__(self, cmd, getter=True, *args):
        self.value = cmd
        self.isInput = getter
        logging.getLogger("logger.main").debug(f"Created a (Input = {self.isInput}) cmd running {self.value}")
        
        
    def __str__(self):
        return self.value
    
    def __bool__(self):
        return self.isInput