class Item:
    def __init__(self, number, id, func):
        self.number = number
        self.id = id
        self.func = func
        
    def listener_func(self, address, *args):
        self.func(self.number, self.id, address, args)