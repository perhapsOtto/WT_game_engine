from circular_queue import CircularQueue
from message import Msg
from terminal import Terminal


class MessageBus():
    
    __queue = CircularQueue(64)
    __listeners = []
    __terminal = Terminal()

    def __init__(self):
        pass

    def post(self, msg:Msg):
        MessageBus.__queue.push(msg)

    def post(self, name:str, info:dict):
        msg = Msg(name, info)
        MessageBus.__queue.push(msg)
    
    def post_imm(self, msg:Msg):
        self.__send_message(msg)
    
    def post_imm(self, name:str, info:dict):
        msg = Msg(name, info)
        self.__send_message(msg)
    
    def register(self, system):
        self.__listeners.append(system)
    
    def unregister(self, system):
        self.__listeners.remove(system)
    
    def __send_message(self, msg:Msg):
        MessageBus.__terminal.write(msg.name)
        for l in MessageBus.__listeners:
            l.handle_message(msg)
    
    def send_all(self): #for testing (maybe)
        for msg in MessageBus.__queue:
            self.__send_message(msg)



def main():
    mb = MessageBus()
    mb.post("PLAY_SOUND", {"id": 100})
    mb.send_all()


if __name__ == "__main__":
    main()
    