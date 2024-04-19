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

# Example usage of Queue
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Front element of the queue:", q.peek())  # Should print 1
print("Dequeued element from the queue:", q.dequeue())  # Should print 1


