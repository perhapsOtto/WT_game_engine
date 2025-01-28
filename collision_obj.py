

class CollisionObj():

    def __init__(self, height, width, shape, active, trigger, gravity=400, mask=[0]):
        self.height = height
        self.width = width
        self.shape = shape
        self.active = active
        self.trigger = trigger
        self.mask = mask
        self.asleep = False
        self.grounded = False
        self.gravity = gravity

    def center(self):
        """returns the [x, y] offset to get the center"""
        return [self.width/2.0, self.height/2.0]

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