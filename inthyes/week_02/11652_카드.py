n = int(input())

a = {}
res = []
for i in range(n):
    x = int(input())
    if x not in a:
        a[x] = 1
    else:
        a[x] += 1

m = max(a.values())

for key, value in a.items():
    if value == m:
        res.append(key)

print(sorted(res)[0])
