from draw_comp import DrawComp
from input_comp import InputComp
from physics_comp import PhysicsComp
from sound_comp import SoundComp

class Root():
    """The big overarching class that starts up all the systems, and is accesible by the game logic"""

    __sound_component:SoundComp = None
    __draw_component:DrawComp = None
    __input_component:InputComp = None
    __pysics_component:PhysicsComp = None
    __scene_component:SceneComp = None