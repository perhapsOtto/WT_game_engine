from collision_obj import CollisionObj
from object import Object
from texture_obj import TextureObj


class RigidBody(Object):

    def __init__(self, x, y, texture, gravity, collision_hight, collision_width, collision_shape, collision_mask=[0], rot=0):
        super().__init__(x, y, rot)
        self.collision = CollisionObj(collision_hight, collision_width, collision_shape, True, False, collision_mask)
        self.texture = TextureObj(texture)
        self.physics = PhysicsObj(gravity)