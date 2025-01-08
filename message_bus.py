from circular_queue import CircularQueue
from message import Msg
from system import System
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
    
    def register(self, system:System):
        self.__listeners.append(system)
    
    def unregister(self, system:System): #might not be needed
        self.__listeners.remove(system)
    
    def send_message(self, msg:Msg):
        MessageBus.__terminal.write(Msg.__mappings[msg.id])
        for l in MessageBus.__listeners:
            l.handle_message(msg)



    