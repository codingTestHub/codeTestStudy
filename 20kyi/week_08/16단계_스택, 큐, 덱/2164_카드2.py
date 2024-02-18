import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque([x for x in range(1, n + 1)])

# for i in range(n):
#     queue.append(i + 1)

while 1:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
    x = queue.popleft()
    queue.append(x)