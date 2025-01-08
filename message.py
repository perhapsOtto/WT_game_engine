

class Msg():
    __mappings = {
        "PLAY_SOUND": 0,
    }
    def __init__(self, name:str, info:dict):
        if name in Msg.__mappings:
            self.id = Msg.__mappings[name]
            self.info = info
        else:
            raise TypeError("unknown message type: " + name)
        