

class Stack:
    def __init__(self):
        self.stack = deque()

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


q = Queue()
q.enqueue(5)
q.enqueue(7)
q.enqueue(2)
q.peek()
q.dequeue()

q.enqueue(3)
q.enqueue(9)
q.enqueue(4)
q.peek()
q.dequeue()
q.dequeue()
print(q)

