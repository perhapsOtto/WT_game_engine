from color import Color


class TextureObj():

    def __init__(self, texture, layer=0, frames_x=1, frames_y=1, looping=False):
        self.sprite = None
        self.texture = texture
        self.fx = frames_x
        self.fy = frames_y
        self.frame = 0
        self.looping = looping
        self.layer = layer
        self.set_frame(0)
        self.tint = Color(0, 0, 0, 1)

    def set_frame(self, frame):
        if frame in range(self.fx * self.xy):
            self.sprite = self.texture #TODO: figure out how this has gotta happen...

    def animate_next(self):
        self.frame += 1
        if self.looping:
            self.frame = self.frame % (self.fx * self.fy)
        elif self.frame >= (self.fx * self.fy):
            return False
        self.set_frame(self.frame)
        return True
    
    def set_tint(self, tint:Color):
        self.tint = tint