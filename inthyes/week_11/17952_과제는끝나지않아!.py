import sys
input = sys.stdin.readline

li, res = [], 0

for _ in range(int(input())):
    x = list(map(int, input().split()))
    if x[0] == 1:
        li.append((x[1], x[2]))

    if li:
        score, time = li.pop()
        time -= 1
        if time == 0:
            res += score
        else:
            li.append((score, time))

print(res)
