from input import Input
from locator import Locator

class SceneComp():
    """keeps track of all the Objects in the scene"""

    #objects = []

    def __init__(self, objects=[]):
        self.objects = objects
        self.spawn_queue = []
        #TODO: uhhhh....

    def add_to_scene(self, object):
        self.objects.append(object)

    def update(self, delta):
        self.spawn_all()
        for obj in Locator.delete_queue:
            self.objects.remove(obj)
            Locator.delete_queue.remove(obj)
        for obj in self.objects:
                obj.update(delta)
        
        return self.objects

    def handle_input(self): #I don't think I need this
        #TODO: uhhhhhhhhhhh
        event = Input.input_queue.pop()
        if event is not None:
            #print("handled:", event)
            for obj in self.objects:
                obj.input(event)
    
    def queue_spawn(self, obj):
        self.spawn_queue.append(obj)
    
    def spawn_all(self):
        for obj in self.spawn_queue:
            self.objects.append(obj)
        self.spawn_queue = []

    