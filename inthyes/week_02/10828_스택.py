from collections import deque
from sys import stdin

input = stdin.readline
n = int(input())
queue = deque()
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        queue.append(cmd[1])

    elif cmd[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
            queue.pop()

    elif cmd[0] == 'size':
        print(len(queue))

    elif cmd[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'top':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])