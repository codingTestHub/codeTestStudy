import sys
input = sys.stdin.readline
n = int(input())
li = []
for i in range(n):
    cmd = input().split()
    if cmd[0] == '1':
       li.append(cmd[1])

    elif cmd[0] == '2':
        if len(li) > 0:
            print(li[-1])
            li.pop()
        else:
            print(-1)

    elif cmd[0] == '3':
        print(len(li))

    elif cmd[0] == '4':
        if len(li) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == '5':
        if len(li) > 0:
            print(li[-1])
        else:
            print(-1)
