from statusCache import Item


class Terminal:
    def __init__(self, statusClass:Item):
        # --CONSTANTS--
        self.refreshToken = "\033[F"
        self.clearToken = "\033[2k"
        # --CONSTANTS--
        
        
        self.infoClass = statusClass
        self.numChannels = statusClass.get_tracked_channels_count()
        self.numItems = statusClass.get_tracked_items_count()
        
    def update(self):
        print(str(self.refreshToken+self.clearToken)*self.numItems)
        self.numItems = self.infoClass.get_tracked_items_count()
        