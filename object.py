

class Object():
    """the base class all game objects inherit"""

    def __init__(self, x, y, rot=0):
        self.x = x
        self.y = y
        self.rot = rot
        self.collision = None
        self.physics = None
        self.texture = None

    def update(self):
        pass