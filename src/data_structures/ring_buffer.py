class RingBuffer:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, item):
        if self.size == self.cap:
            self.head = (self.head + 1) % self.cap # overwrite oldest
        else:
            self.size += 1
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.cap

    def pop(self):
        if self.size == 0: raise IndexError("buffer is empty")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.cap
        self.size -= 1
        return item
