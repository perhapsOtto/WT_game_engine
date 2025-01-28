from input import Input
from locator import Locator

class Object():
    """the base class all game objects inherit"""

    def __init__(self, x, y, rot=0):
        self.x = x
        self.y = y
        self.rot = rot
        self.weight = 0
        self.velocity = [0, 0]
        self.old_velocity = [0, 0]
        self.collision = None
        self.physics = None
        self.texture = None
        self.asleep = False
        self.static = True
        #self.grounded = False

    def update(self, delta):
        if Input.event is not None:
            print("update input check", Input.event)
        

    def input(self, event):
        print("input on", self, event)

    def check_sleep(self):
        if (abs(self.velocity[0]) < 0.1 and abs(self.velocity[1]) < 0.1 and 
            abs(self.old_velocity[0]) < 0.1 and abs(self.old_velocity[1]) < 0.1):
            self.asleep = True
        else:
            self.sleep = False

    def move(self, delta):
        self.x += self.velocity[0] * delta
        self.y += self.velocity[1] * delta
        self.old_velocity = self.velocity
    
    def gravity(self, delta):
        if not self.static and self.collision is not None:
            if not self.collision.grounded:
                self.velocity[1] -= self.collision.gravity*delta
                if self.velocity[1] < self.collision.gravity*-2.0:
                    self.velocity[1] = self.collision.gravity*-2.0
            elif self.velocity[1] < 0.0:
                self.velocity[1] = 0
    
    def queue_free(self):
        Locator.queue_free(self)
