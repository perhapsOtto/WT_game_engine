from color import Color
from window import Window
from render_copy import Draw#changebacklater
import glfw


class DrawComp():
    """handles drawing for root"""

    def __init__(self, window, resources):
        self.wind_manager = Window()
        #with self.wind_manager.create_main_window(w, h, title) as self.window:
        self.window = window
        dim = glfw.get_window_size(window) #kinda silly?
        self.draw = Draw(dim[0], dim[1])
        #    self.tes = self.window
        #    #self.wind_manager.main_loop(self.window)

    def render_scene(self, objs, camera):
        self.draw.clear()
        for obj in objs:
            if obj.texture == "COLOR_RECT":
                self.draw_square((obj.x-camera.x)*camera.zoom, (obj.y-camera.y)*camera.zoom, (obj.height)*camera.zoom, (obj.width)*camera.zoom, obj.color)
        self.wind_manager.swap(self.window)


    def draw_sprite(self, texture, posx, posy, rot=0, tint=[0,0,0,1]):
        """tells the renderer to draw sprite at position (posx, posy)with a rotation of rot(in degrees (clockwise)) and a tint of tint"""
        #TODO: figure out OpenGL D:
        pass

    def draw_square(self, posx, posy, height, width, color):
        """draws a square of color at position (posx, posy), with height and width"""
        self.draw.drawSquare(posx, posy, width, height, color) #don't love this conversion...

    def draw_elipse(self, posx, posy, height, width, color):
        """draws a elipse of color at position (posx, posy), with height and width"""
        #TODO: more more OpenGL
        pass

    def draw_line(self, posx1, posy1, posx2, posy2, thinkness, color):
        """draws a line from pos1 to pos2 of color with a thickness of thickness"""
        self.draw.drawLine(posx1, posy1, posx2, posy2, color) #don't love this conversion...

    def test(self):
        while (
            glfw.get_key(self.window, glfw.KEY_ESCAPE) != glfw.PRESS and
            not glfw.window_should_close(self.window)
        ):
            self.wind_manager.swap(self.window)
            self.draw_square(20, 20, 20, 20, [1, 1, 1, 1])


if __name__ == "__main__":
    with Window().create_main_window(200, 300, "title") as window:
        d = DrawComp(window, None)
        d.test()

# w = Window()    
# with w.create_main_window() as window:
#     while (
#             glfw.get_key(window, glfw.KEY_ESCAPE) != glfw.PRESS and
#             not glfw.window_should_close(window)
#         ):
#         w.swap(window)


