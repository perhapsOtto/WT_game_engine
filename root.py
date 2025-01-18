from draw_comp import DrawComp
from input import Input
from keyboard_input_mac import SimpleInputMac
from locator import Locator
from physics_comp import PhysicsComp
from resources import Resources
from scene_comp import SceneComp

from object import Object #temp for testing


class Root():
    """The big overarching class that starts up all the systems, and is accesible by the game logic"""

    __locator:Locator = None
    __draw_component:DrawComp = None
    __input_component:Input = None
    __physics_component:PhysicsComp = None
    __scene_component:SceneComp = None
    __recources:Resources = None

    key_mappings = {"a": "left", "w": "up", "s":"down", "d": "right"} #temp

    def __init__(self):
        Root.__input_component = SimpleInputMac(Root.key_mappings)
        lst = []
        lst.append(Object(0, 0))
        lst.append(Object(3, 5))
        Root.__scene_component = SceneComp(lst)
        self.loop()

    def loop(self):

        while 1:
            Root.__input_component.get_input()
            Root.__scene_component.handle_input()#temp
            objs = Root.__scene_component.update()
            #Root.__physics_component.process(objs) #uhh kinda a lot of coupling...
            Root.__draw_component.render_scene(objs)

this = Root()