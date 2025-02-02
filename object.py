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
        self.texture = None
        self.listeners = {}

    def update(self, delta):
        '''called every frame by scene'''
        pass
        

    def input(self, event):
        print("input on", self, event)

    def check_sleep(self):
        '''check if self should be chacked by the physics system'''
        if (abs(self.velocity[0]) < 0.1 and abs(self.velocity[1]) < 0.1 and 
            abs(self.old_velocity[0]) < 0.1 and abs(self.old_velocity[1]) < 0.1):
            self.asleep = True
        else:
            self.sleep = False

    def move(self, delta):
        '''move by velocity'''
        self.x += self.velocity[0] * delta
        self.y += self.velocity[1] * delta
        self.old_velocity = self.velocity
    
    def gravity(self, delta):
        '''apply gravity'''
        if not self.static and self.collision is not None:
            if not self.collision.grounded:
                self.velocity[1] -= self.collision.gravity*delta
                if self.velocity[1] < self.collision.gravity*-2.0:
                    self.velocity[1] = self.collision.gravity*-2.0
            elif self.velocity[1] < 0.0:
                self.velocity[1] = 0
    
    def queue_free(self):
        '''queue self to be deleted'''
        Locator.queue_free(self)

    def connect(self, obj, func_name):
        '''connect obj.func_name to be called when emit() is run'''
        self.listeners[obj] = func_name
    
    def emit(self):
        '''calls the functions on all self's listeners'''
        for obj in self.listeners.keys():
            func = getattr(obj, self.listeners[obj])
            func()
    

