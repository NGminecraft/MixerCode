from statusCache import Item
import os
import sys
import logging
from KeyLogger import KeyLogger
import asyncio


class Terminal:
    def __init__(self, infoClass:Item):
        # --CONSTANTS--
        self.lineChange = "\033[F"
        self.clearToken = "\033[2K"
        self.terminalPrefix = "\033[?1049h"
        # --CONSTANTS--
        
        self.logger = logging.getLogger("logger.main")
        
        self.keyLogger = KeyLogger(infoClass.track_channel_value)
        
        self.infoClass = infoClass
        self.numChannels = infoClass.get_tracked_channels_count()
        self.numItems = infoClass.get_tracked_items_count()
        self.first = True
        print(self.terminalPrefix)
        
    def check_channels(self):
        if self.infoClass.get_tracked_channels_count() != self.numChannels:
            self.numChannels = self.infoClass.get_tracked_channels_count()
        
    def update(self):
        sys.stdout.write(str(self.lineChange+self.clearToken)*(self.numItems+2)) # Clears Old data
        self.numItems = self.infoClass.get_tracked_items_count()
        self.check_channels()
        
        # --PRINTING DATA--
        width_per_channel = (os.get_terminal_size()[0] - self.numChannels-1) // self.numChannels
        
        ids = self.infoClass.get_tracked_items()
        
        full_list = []
        for j in ids:
            row_list = []
            for i in range(1, self.numChannels+1):
                toAdd = f"{j}: {self.infoClass.get_value_of_channel(i, j)}"
                row_list.append(toAdd+(' '*(width_per_channel-len(toAdd))))
            full_list.append("#".join(row_list))
        sys.stdout.write("\n".join(full_list))
        sys.stdout.write("\n")
        sys.stdout.write("\033[2K\r: ")
        sys.stdout.write(self.keyLogger.typed_string)
        sys.stdout.flush()