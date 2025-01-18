

class Resources():

    resources = {}
    path = "test"
    #could be seperate dicts.. maybe...

    def __init__(self, dir):
        self.path = dir
        pass

    def load(self, file):
        #TODO: learn the file system
        pass

    def access(self, file):
        return Resources.resources[file]

