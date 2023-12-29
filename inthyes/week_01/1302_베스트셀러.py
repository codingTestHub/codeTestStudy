n = int(input())
a = {}
res = []

for _ in range(n):
    name = input()
    if name not in a:
        a[name] = 1
    else:
        a[name] += 1

m = max(a.values())

for key, value in a.items():
    if value == m:
        res.append(key)

sorted_res = sorted(res)
print(sorted_res[0])