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
        self.logger.info(f"Started tracking {len(self.channels)} channels")

    def track_channel_value(self, channel, cmd:str|CMD, id=None):
        """If command is sent as string, use 00 to signify each channel"""
        channel = format(channel(num=channel, width=2))
        if type(cmd) is str:
            cmd = CMD(cmd.replace("00", str(channel)), True)
        if not id:
            id = cmd.value
        for i in self.channels:
            self.values[i].append(0)
            self.tracker_register(Item(i, self.value).listener_func, cmd)
        self.valuesId.append(id)
            
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
             
    