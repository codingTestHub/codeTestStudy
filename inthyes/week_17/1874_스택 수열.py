n = int(input())

cnt = 1
temp = True
stack = []
res = []

for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        res.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        res.append('-')
    else:
        temp = False

if temp == False:
    print('NO')
else:
    for i in res:
        print(i)