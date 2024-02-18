# ???
import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    stack = []
    vps = input()

    for j in vps:
        if j == '(':  # '(' 괄호 들어오면 stack에 넣기
            stack.append(j)
            # print(stack)
        elif j == ')':  # ')' 괄호 들어왔을떄
            if stack:  # stack이 비어있지 않다면 pop
                stack.pop()
                # print(stack)
            else:  # stack이 비어있다면 "NO"
                print("NO")
                break
    else:  # for문에서 break가 없을 때
        if not stack:  # stack이 비어있다면 모두 짝이 맞은 경우 => YES
            print("YES")
        else:  # stack에 괄호가 남아있다면 짝이 맞지 않음 => NO
            print("NO")
