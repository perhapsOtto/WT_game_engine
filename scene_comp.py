from input import Input

class SceneComp():
    """keeps track of all the Objects in the scene"""

    #objects = []

    def __init__(self, objects=[]):
        self.objects = objects
        #TODO: uhhhh....
        pass

    def add_to_scene(self, object):
        self.objects.append(object)

    def update(self):
        for obj in self.objects:
                obj.update()
        
        return self.objects

    def handle_input(self):
        #TODO: uhhhhhhhhhhh
        event = Input.input_queue.pop()
        if event is not None:
            #print("handled:", event)
            for obj in self.objects:
                obj.input(event)
        
        pass