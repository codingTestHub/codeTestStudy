n = int(input())
cnt = 0

for _ in range(n):
    x = input()
    stack = []

    for i in range(len(x)):
        if stack and x[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(x[i])

    if not stack:
        cnt += 1

print(cnt)

