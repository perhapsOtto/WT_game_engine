

class Msg():
    __mappings = {
        "PLAY_SOUND": 0,
        "DRAW_SPRITE": 1,
        
    }
    def __init__(self, name:str, info:dict):
        if name in Msg.__mappings:
            self.name = name
            self.id = Msg.__mappings[name]
            self.info = info
        else:
            raise TypeError("unknown message type: " + name)
    
    def get_mappings(self):
        return self.__mappings
        