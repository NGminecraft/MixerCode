from statusCache import Item
import os
import logging


class Terminal:
    def __init__(self, infoClass:Item):
        # --CONSTANTS--
        self.lineChange = "\033[F"
        self.clearToken = "\033[2K"
        # --CONSTANTS--
        
        self.logger = logging.getLogger("logger.main")
        
        
        self.infoClass = infoClass
        self.numChannels = infoClass.get_tracked_channels_count()
        self.numItems = infoClass.get_tracked_items_count()
        
    def check_channels(self):
        if self.infoClass.get_tracked_channels_count() != self.numChannels:
            self.numChannels = self.infoClass.get_tracked_channels_count()
        
    def update(self):
        print(str(self.refreshToken+self.clearToken)*self.numItems) # Clears Old data
        self.numItems = self.infoClass.get_tracked_items_count()
        self.check_channels()
        
        # --PRINTING DATA--
        width_per_channel = (os.get_terminal_size()[0] - self.numChannels-1) // self.numChannels
        
        ids = self.infoClass.get_tracked_items()
        
        full_list = []
        for i in range(1, self.numChannels+1):
            row_list = []
            for j in ids:
                toAdd = f"{j}: {self.infoClass.get_value_of_channel(i, j)}"
                row_list.append(toAdd+(' '*(width_per_channel-len(toAdd))))
            full_list.append("#".join(row_list))
        print("\n".join(full_list))
            