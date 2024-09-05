from statusCache import Item
from os import terminal_size


class Terminal:
    def __init__(self, statusClass:Item):
        # --CONSTANTS--
        self.refreshToken = "\033[F"
        self.clearToken = "\033[2k"
        # --CONSTANTS--
        
        
        self.infoClass = statusClass
        self.numChannels = statusClass.get_tracked_channels_count()
        self.numItems = statusClass.get_tracked_items_count()
        
    def check_channels(self):
        if self.statusClass.get_tracked_channels_count() != self.numChannels:
            self.numChannels = self.statusClass.get_tracked_channels_count()
        
    def update(self):
        print(str(self.refreshToken+self.clearToken)*self.numItems)
        self.numItems = self.infoClass.get_tracked_items_count()
        self.check_channels()
        width_per_channel = (terminal_size.columns - self.numChannels-1) // self.numChannels
        
        items = self.statusClass.get_value_of_channel()
        dict_keys = list(items[0].keys())
        
        full_list = []
        for i in dict_keys:
            row_list = []
            for j in items:
                toAdd = f"{i}: {j[i]}"
                row_list.append(toAdd+(' '*width_per_channel-len(toAdd)))
            full_list.append("#".join(row_list))
        print("\n".join(full_list))
            