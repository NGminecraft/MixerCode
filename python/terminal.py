from statusCache import Item


class Terminal:
    def __init__(self, statusClass:Item):
        self.infoClass = statusClass
        self.numChannels = statusClass.get_tracked_channels_count()
        
        
    
    
    def update(self):
        pass
