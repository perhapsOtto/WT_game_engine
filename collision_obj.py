

class CollisionObj():
    '''collision shape and dimensions to be attached to objects'''

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
        '''turns the collision shape on'''
        self.active = True
    
    def deactivate(self):
        '''turns the collision shape off'''
        self.active = False

    def is_active(self):
        '''checks if self is active'''
        return self.active
    
    def add_mask(self, layer:int):
        '''adds layer to list of masks, cerrently does nothing'''
        if layer not in self.mask:
            self.mask.append(layer)

    def remove_mask(self, layer:int):
        '''removes layer from list of masks, cerrently does nothing'''
        if layer in self.mask:
            self.mask.remove(layer)