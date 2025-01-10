

class CollisionObj():

    def __init__(self, hight, width, shape, active, trigger, mask=[0]):
        self.hight = hight
        self.width = width
        self.shape = shape
        self.active = active
        self.trigger = trigger
        self.mask = mask

    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False

    def is_active(self):
        return self.active
    
    def add_mask(self, layer:int):
        if layer not in self.mask:
            self.mask.append(layer)

    def remove_mask(self, layer:int):
        if layer in self.mask:
            self.mask.remove(layer)