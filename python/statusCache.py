import logging
from utilClasses.communicationHandler import Item
from utilClasses.cmd import CMD


class Status:
    def __init__(self, handler_register, num_channels:int|None, channels: list[int]|tuple|None = None):
        self.logger = logging.getLogger("logger.main")
        if not num_channels:
            self.channels = set(range(1, 17))
        elif channels:
            self.channels = set(channels)
        elif not channels:
            self.channels = set(range(1, num_channels+1))
            
        self.tracked_items_count = 0
        
        self.tracker_register = handler_register
            
        self.values = {}
        self.valuesId = []
        for i in self.channels:
            self.values[i] = []
        self.track_channel_value("/ch/00/config/name", "Name")
        

    def track_channel_value(self, cmd:str, id=None):
        """If command is sent as string, use 00 to signify each channel"""
        if not id:
            id = cmd.value
        id += ": "
        for i in self.channels:
            self.values[i].append(0)
            self.tracker_register(Item(i, self.value).listener_func, CMD(cmd.replace("00", str(i)), True))
        self.valuesId.append(id)
        self.logger.info(f"Started tracking the value of {id} for {len(self.get_tracked_channels_count())} channels")
            
    def get_tracked_items(self):
        return self.valuesID
        
    def get_tracked_items_count(self):
        return len(self.valuesId)
            
    def set_value(self, channel, address, value):
        self.values[channel] = value
        
    def get_value_of_channel(self, channelValue:int|list[int]|None = None):
        if not channelValue:
            return self.values.values()
        elif type(channelValue) is int:
            return self.values[channelValue]
        else:
            return [self.values[i] for i in channelValue]
        
    def get_tracked_channels(self):
        return self.channels
    
    def get_tracked_channels_count(self):
        return len(self.channels)
             
    