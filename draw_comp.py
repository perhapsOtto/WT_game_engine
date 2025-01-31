from color import Color
from window import Window
from render.render import Render
import glfw


class DrawComp():
    """handles drawing for root"""

    def __init__(self, window, resources):
        self.window_class = window
        self.window = self.window_class.window

        dim = glfw.get_window_size(self.window) #kinda silly?
        self.renderer = Render(self.window_class)

        self.window_class.make_context()
        #    self.tes = self.window
        #    #self.wind_manager.main_loop(self.window)

    def render_scene(self, objs, camera):
        self.renderer.clear()
        for obj in objs:
            if obj.texture == "COLOR_RECT":
                self.draw_square((obj.x-camera.x)*camera.zoom, (obj.y-camera.y)*camera.zoom, (obj.height)*camera.zoom, (obj.width)*camera.zoom, obj.color)
            else:
                self.draw_sprite(obj.texture, (obj.x-camera.x)*camera.zoom, (obj.y-camera.y)*camera.zoom, (obj.height)*camera.zoom, (obj.width)*camera.zoom, obj.animator)
        self.window_class.swap()


    def draw_sprite(self, texture, posx, posy, height, width, animator, tint=[0,0,0,1]):
        """tells the renderer to draw sprite at position (posx, posy)with a rotation of rot(in degrees (clockwise)) and a tint of tint"""

        self.renderer.draw_sprite(posx, posy, width, height, texture, animator)

    def draw_square(self, posx, posy, height, width, color):
        """draws a square of color at position (posx, posy), with height and width"""
        self.renderer.draw_color_rect(posx, posy, width, height, color)

    def draw_elipse(self, posx, posy, height, width, color):
        """draws a elipse of color at position (posx, posy), with height and width"""
        #TODO: more more OpenGL
        pass

    def draw_line(self, posx1, posy1, posx2, posy2, thinkness, color):
        """draws a line from pos1 to pos2 of color with a thickness of thickness"""
        pass#self.draw.drawLine(posx1, posy1, posx2, posy2, color)

    def test(self):
        while (
            glfw.get_key(self.window, glfw.KEY_ESCAPE) != glfw.PRESS and
            not glfw.window_should_close(self.window)
        ):
            self.wind_manager.swap(self.window)
            self.draw_square(20, 20, 20, 20, [1, 1, 1, 1])


# w = Window()    
# with w.create_main_window() as window:
#     while (
#             glfw.get_key(window, glfw.KEY_ESCAPE) != glfw.PRESS and
#             not glfw.window_should_close(window)
#         ):
#         w.swap(window)


