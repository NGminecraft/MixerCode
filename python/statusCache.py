import logging
from communicationHandler import Item
from cmd import CMD


class Status:
    def __init__(self, handler_register, num_channels:int|None, channels: list[int]|tuple|None = None):
        self.logger = logging.getLogger("logger.main")
        if not num_channels:
            self.channels = set(range(1, 17))
        elif channels:
            self.channels = set(channels)
        elif not channels:
            self.channels = set(range(1, num_channels+1))
            
        self.values = {}
        for i in self.channels:
            self.values[i] = 0
            handler_register(Item(i, self.value).listener_func, CMD(f"meters/{format(num=i, width=2)}", True))
            
        self.logger.info(f"Started tracking {len(self.channels)} channels")
            
    def set_value(self, channel, address, value):
        self.values[channel] = value
        