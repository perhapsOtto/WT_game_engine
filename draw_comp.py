from color import Color


class DrawComp():
    """handles drawing for root"""

    def __init__(self, resources):
        #TODO: make the whole thing...
        pass

    def draw_sprite(self, texture, posx, posy, rot=0, tint=Color(0,0,0,1)):
        """tells the renderer to draw sprite at position (posx, posy)with a rotation of rot(in degrees (clockwise)) and a tint of tint"""
        #TODO: figure out OpenGL D:
        pass

    def draw_square(self, posx, posy, height, width, color:Color):
        """draws a square of color at position (posx, posy), with height and width"""
        #TODO: more OpenGL
        pass

    def draw_elipse(self, posx, posy, height, width, color:Color):
        """draws a elipse of color at position (posx, posy), with height and width"""
        #TODO: more more OpenGL
        pass

    def draw_line(self, pos1, pos2, thinkness, color:Color):
        """draws a line from pos1 to pos2 of color with a thickness of thickness"""
        #TODO: more more more OpenGL
        pass

    

