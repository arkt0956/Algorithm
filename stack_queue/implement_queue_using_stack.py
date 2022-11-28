class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self,x: int):
        self.input.append(x)

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def empty(self):
        return len(self.input) == 0 and len(self.output) == 0

queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.empty())
