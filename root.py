import time
from camera import Camera
from draw_comp import DrawComp
from glfw_input import glfwInput
from input import Input
from locator import Locator
from physics_comp import PhysicsComp
from resources import Resources
from scene_comp import SceneComp
from audio import Audio
from scene_tests import Scenes

from window import Window


class Root():
    """The big overarching class that starts up all the systems, and handles the main loop"""

    __locator:Locator = None
    __draw_component:DrawComp = None
    __input_component:Input = None
    __physics_component:PhysicsComp = None
    __scene_component:SceneComp = None
    __recources:Resources = None
    __audio:Audio = None

    key_mappings = {"A": "left", "W":"up", "S":"down", "D":"right", "ESC":"close", "UP" : "z_in", "DOWN" : "z_out", "LEFT" : "cam_left", "RIGHT": "cam_right"} #temp

    def __init__(self):
        scene = Scenes.scene1()
        lst = scene[0]
        ui = scene[1]
        Root.__scene_component = SceneComp(lst)
        Root.__scene_component.ui = ui
        Locator.provide_scene(Root.__scene_component)
        window_class = Window(400, 400, "TESTING NEW RENDERER")
        window_class.make_context()
        Root.__draw_component = DrawComp(window_class, Root.__recources, [0.7, 0.8, 0.9, 1])
        Root.__input_component = glfwInput(Root.key_mappings, window_class)
        Root.__physics_component = PhysicsComp(Root.__input_component)
        Locator.provide_input(Root.__input_component)
        self.loop()

    def loop(self):
        '''the main loop'''
        time_start = time.time()
        camera = Camera(400, 400)
        while 1:
            delta = time.time() - time_start
            time_start = time.time()

            test_input = Root.__input_component.get_input()

            if "close" in test_input["just_pressed"]: #yeah, this isn't great...
                break

            if "z_in" in test_input["held"]:
                camera.zoom += delta*0.5
            elif "z_out" in test_input["held"]:
                camera.zoom -= delta*0.5
            
            if "cam_right" in test_input["held"]:
                camera.x += 50*delta
            elif "cam_left" in test_input["held"]:
                camera.x -= 50*delta            

            objs = Root.__scene_component.update(delta)

            Root.__physics_component.move(objs, delta, Root.__scene_component.ui)
            Root.__draw_component.render_scene(objs, camera, Root.__scene_component.ui)

if __name__ == "__main__":
    this = Root()