

class Terminal():
    filename = "terminal.txt"

    def __init__(self, filename="terminal.txt"):
        Terminal.filename = filename
        self.file = open(Terminal.filename, 'w')
        self.file.write("--Terminal--\n")
    
    def write(self, line):
        self.file.write(line + "\n")