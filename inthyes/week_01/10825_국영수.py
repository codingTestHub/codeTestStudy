n = int(input())

li = []
for i in range(n):
    [name, a, b, c] = map(str, input().split())
    li.append([name, int(a), int(b), int(c)])

sorted_li = sorted(li, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in sorted_li:
    print(i[0])