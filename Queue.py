# to perform operations like append(), appendleft(), pop(), and popleft() on a double-ended queue.
from collections import deque

queue = deque()
queue.append("1")
queue.append("2")
queue.appendleft("0")
queue.enqueue("5")
print(queue)

while len(queue) > 0:
    removed = queue.popleft()
    print(f'printing{item}')

print(queue)