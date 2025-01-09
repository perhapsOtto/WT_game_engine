

class CircularQueue():
    """A queue that links back up to its start"""

    def __init__(self, max_size):
        """Create a queue, with a maximum size of max_size"""
        self.__head = 0
        self.__tail = 0
        self.__max_size = max_size
        self.__queue = [' '] * max_size
    
    def push(self, item):
        """Add an item to the queue, throws an error if there's not enough space in the queue"""
        if (self.__tail + 1) % self.__max_size != self.__head:
            self.__queue[self.__tail] = item
            self.__tail = (self.__tail + 1) % self.__max_size
        else:
            raise MemoryError("not enough space in queue of size: " + self.__max_size + " to add item: " + item)
    
    def pop(self):
        """Removes and returns the first element of the queue.
        If the queue is empty, returns None"""
        if self.__head != self.__tail:
            item = self.__queue[self.__head]
            self.__head = (self.__head + 1) % self.__max_size
            return item
        else:
            return None
    
    def size(self):
        """Returns the size of queue"""
        if self.__head == self.__tail:
            return 0
        return self.__max_size - (self.__head - self.__tail) % self.__max_size

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__head == self.__tail:
            raise StopIteration
        return self.pop()

