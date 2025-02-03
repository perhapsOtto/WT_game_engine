from collision_obj import CollisionObj
from object import Object
from texture_obj import TextureObj


class Terrain(Object):
    '''a base class for an object unaffected by movement'''

    def __init__(self, x, y, texture, collision_hight, collision_width, collision_shape, collision_mask=[0], rot=0):
        super().__init__(x, y, rot)
        """creates a terrain object at position (x, y), with a collision box of dimensions (collision_hight, width) with shape collision shape"""
        self.collision = CollisionObj(collision_hight, collision_width, collision_shape, True, False, collision_mask)
        self.texture = TextureObj(texture)
        