class Item:
    def __init__(self, id, func):
        self.id = id
        self.func = func
        
    def listener_func(self, address, *args):
        self.func(self.id, address, args)