import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
deque = deque([])

for i in range(n):
    command = input().split()

    if command[0] == '1':
        deque.appendleft(command[1])  # 앞에서 입력

    elif command[0] == '2':
        deque.append(command[1])  # 뒤에서 입력

    elif command[0] == '3':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())  # 맨 앞의 정수 빼고 출력

    elif command[0] == '4':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())  # 맨 뒤의 정수 빼고 출력

    elif command[0] == '5':
        print(len(deque))  # 덱에 있는 정수 개수 출력

    elif command[0] == '6':
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == '7':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])  # 덱의 맨 앞에 있는 정수 출력

    elif command[0] == '8':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])  # 덱의 맨 뒤에 있는 정수 출력
