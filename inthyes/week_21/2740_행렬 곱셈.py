m1 = []
m2 = []
a, b = map(int, input().split())
for _ in range(a):
    m1.append(list(map(int, input().split())))
b, c = map(int, input().split())
for _ in range(b):
    m2.append(list(map(int, input().split())))
m2 = [[x[i] for x in m2] for i in range(len(m2[0]))]

for i in range(a):
    for j in range(c):
        ans = 0
        for k in range(b):
            ans += m1[i][k] * m2[j][k]
        print(ans, end = " ")
    print()
