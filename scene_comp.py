from input import Input
from locator import Locator

class SceneComp():
    """keeps track of all the Objects in the scene"""

    #objects = []

    def __init__(self, objects=[]):
        self.objects = objects
        self.spawn_queue = []
        self.ui = []

    def add_to_scene(self, object):
        '''adds object to the current scene'''
        self.objects.append(object)

    def update(self, delta):
        '''calls update on all the objects in the scene, and deletes objects queued for deletion'''
        self.spawn_all()
        for obj in Locator.delete_queue:
            self.objects.remove(obj)
            Locator.delete_queue.remove(obj)
        for obj in self.objects:
                obj.update(delta)
        for elt in self.ui:
            elt.update(delta)
        
        return self.objects
    
    def queue_spawn(self, obj):
        '''queues obj to be spawned on the next frame'''
        self.spawn_queue.append(obj)
    
    def spawn_all(self):
        '''spawns all objects currently in the spawn queue'''
        for obj in self.spawn_queue:
            self.objects.append(obj)
        self.spawn_queue = []

    