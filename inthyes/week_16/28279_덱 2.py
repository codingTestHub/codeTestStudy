from collections import deque
import sys
queue = deque()
for i in range(int(input())):
    command = list(map(int, sys.stdin.readline().rstrip().split()))
    l = len(queue)

    if command[0] == 1:
        queue.appendleft(command[1])
    elif command[0] == 2:
        queue.append((command[1]))
    elif command[0] == 3:
        if l:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == 4:
        if l:
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == 5:
        print(len(queue))
    elif command[0] == 6:
        if l:
            print(0)
        else:
            print(1)
    elif command[0] == 7:
        if l:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 8:
        if l:
            print(queue[-1])
        else:
            print(-1)
