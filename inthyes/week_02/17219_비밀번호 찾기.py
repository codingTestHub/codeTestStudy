import sys
input = sys.stdin.readline
n, m = map(int,input().split())
pwd = {}
res = []
for _ in range(n):
    x = input().split()
    pwd[x[0]] = x[1]
for i in range(m):
    y = input().strip()
    if y in pwd:
        print(pwd[y])