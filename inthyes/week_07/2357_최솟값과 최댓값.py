n, m = map(int, input().split())
li = []
for _ in range(n):
    li.append(int(input()))

for _ in range(m):
    a, b = map(int, input().split())
    Max = li[a-1]
    Min = li[a-1]
    for i in range(a-1, b):
        if li[i] > Max:
            Max = li[i]
        if li[i] < Min:
            Min = li[i]
    print(Min, Max)