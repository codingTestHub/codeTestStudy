mes = input()
n = int(input())
res = 0
for i in range(n):
    x = input()
    if mes in x * 2:
        res += 1
        continue
print(res)