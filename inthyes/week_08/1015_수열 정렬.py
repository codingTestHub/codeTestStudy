n = int(input())
li = list(map(int, input().split()))
s_li = sorted(li)

x = []
for i in range(n):
    idx = s_li.index(li[i])
    x.append(idx)
    s_li[idx] = -1
print(*x)