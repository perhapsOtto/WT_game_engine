import time
from camera import Camera
from color_rect import ColorRect
from draw_comp import DrawComp
from glfw_input import glfwInput
from input import Input
from locator import Locator
from physics_comp import PhysicsComp
from resources import Resources
from scene_comp import SceneComp

from object import Object
from squaracter import Squaracter
from window import Window


class Root():
    """The big overarching class that starts up all the systems, and is accesible by the game logic"""

    __locator:Locator = None
    __draw_component:DrawComp = None
    __input_component:Input = None
    __physics_component:PhysicsComp = None
    __scene_component:SceneComp = None
    __recources:Resources = None

    key_mappings = {"A": "left", "W":"up", "S":"down", "D":"right", "ESC":"close", "UP" : "z_in", "DOWN" : "z_out", "LEFT" : "cam_left", "RIGHT": "cam_right"} #temp

    def __init__(self):
        lst = []
        lst.append(Squaracter(0, 180, 50, 50, [1, 1, 1, 1], 100))
        lst.append(ColorRect(200, 200, 50, 50, [0, 0.5, 1, 1]))
        lst.append(ColorRect(0, 20, 400, 20, [1, 0.5, 0, 1]))
        #lst.append(ColorRect(100, 10, 20, 200, [1, 0, 0.2, 1]))
        lst[1].weight = 500
        #lst[1].static = True
        lst[2].static = True
        Root.__scene_component = SceneComp(lst)
        Locator.provide_scene(Root.__scene_component)
        with Window().create_main_window(400, 400, "title!") as window:
            Root.__draw_component = DrawComp(window, Root.__recources)
            Root.__input_component = glfwInput(Root.key_mappings, Root.__draw_component.window)
            Root.__physics_component = PhysicsComp()
            Locator.provide_input(Root.__input_component)
            self.loop()

    def loop(self):
        time_start = time.time()
        camera = Camera(400, 400)
        while 1:
            delta = time.time() - time_start
            time_start = time.time()
            #print(delta)

            test_input = Root.__input_component.get_input()
            #for i in test_input:
            #    #print(i)
            #    if i == "close":
            #        close = True
            if "close" in test_input["just_pressed"]:
                break

            if "z_in" in test_input["held"]:
                camera.zoom += delta*0.5
            elif "z_out" in test_input["held"]:
                camera.zoom -= delta*0.5
            
            if "cam_right" in test_input["held"]:
                camera.x += 50*delta
            elif "cam_left" in test_input["held"]:
                camera.x -= 50*delta            

            #Root.__scene_component.handle_input()#temp
            objs = Root.__scene_component.update(delta)

            #temp, tesing physics
            #objs[0].velocity[0] = 200*test_input[0]
            #if objs[0].collision.grounded and test_input[1] > 0:
            #    jump_start = time.time()
            #    objs[0].velocity[1] = 200
            #elif time.time()-jump_start < 0.5 and test_input[1] > 0:
            #    objs[0].velocity[1] += 300*delta

            Root.__physics_component.move(objs, delta) #uhh kinda a lot of coupling...
            Root.__draw_component.render_scene(objs, camera)

this = Root()