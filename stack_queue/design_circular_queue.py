import collections


class MyCircularQueue:
    def __init__(self, k: int):
        self.length = k
        self.queue = [None] * self.length
        self.f = 0
        self.r = 0

    def enqueue(self, x: int) -> bool:
        if self.queue[self.r] is None:
            self.queue.append(x)
            self.r = (self.r + 1) % self.length
            return True
        else:
            return False

    def rear(self) -> int:
        return self.queue[self.r]

    def isfull(self) -> bool:
        return self.f + 1 == self.r

    def dequeue(self) -> bool:
        if self.queue[self.f] is not None:
            self.queue[self.f] = None
            self.f = (self.f + 1) % self.length
            return True
        else:
            return False

    def front(self) -> int:
        return self.queue[self.f]

