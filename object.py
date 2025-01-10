

class Object():
    """the base class all game objects inherit"""

    def __init__(self, x, y, rot=0):
        self.x = x
        self.y = y
        self.rot = rot

    def update(self):
        pass