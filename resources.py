

class Resources():
    '''holds all the needed files, like textures and sounds, currently unimplemented'''

    resources = {}
    path = "test"
    #could be seperate dicts.. maybe...

    def __init__(self, dir):
        Resources.path = dir
        pass

    def load(self, file):
        #TODO: everything...
        pass

    def access(self, file):
        return Resources.resources[file]

