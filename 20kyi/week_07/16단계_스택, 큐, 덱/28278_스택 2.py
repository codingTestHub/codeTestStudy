import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    command = input().split()

    if command[0] == '1':   # 정수 x를 스택에 입력
        stack.append(command[1])

    elif command[0] == '2': # 스택에 정수가 있다면 맨위 정수 빼고 출력, 없으면 -1
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif command[0] == '3': # 스택에 들어있는 정수 개수 출력
        print(len(stack))

    elif command[0] == '4': # 스택 비어있으면 1, 아니면 0
        if stack:
            print(0)
        else:
            print(1)

    elif command[0] == '5': # 스택에 정수가 있다면 맨위의 정수 출력, 없으면 -1
        if stack:
            print(stack[-1])
        else:
            print(-1)
