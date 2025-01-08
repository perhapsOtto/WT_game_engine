
from message import Msg
from message_bus import MessageBus
from abc import ABC, abstractmethod #maybe?


class System(ABC):
    """The abstract class for all the systems to extend"""

    __msg_bus = MessageBus()

    def __init__(self):
        System.__msg_bus.register(self)

    @abstractmethod
    def handle_message(msg:Msg):
        pass