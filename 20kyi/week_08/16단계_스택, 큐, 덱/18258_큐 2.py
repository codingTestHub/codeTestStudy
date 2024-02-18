import sys
from collections import deque

n = int(input())
queue = deque([])

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.append(command[1])  # 정수 X를 큐에 넣음

    elif command[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())  # 큐에서 가장 앞에 있는 정수를 뺌

    elif command[0] == 'size':
        print(len(queue))  # 큐에 들어있는 정수의 개수를 출력

    elif command[0] == 'empty':
        if len(queue) == 0:  # 큐가 비어있으면 1,
            print(1)
        else:  # 아니면 0을 출력
            print(0)

    elif command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])  # 큐의 가장 앞에 있는 정수

    elif command[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])  # 큐의 가장 뒤에 있는 정수
