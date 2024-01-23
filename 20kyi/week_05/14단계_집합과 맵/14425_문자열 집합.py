import sys

n, m = map(int, sys.stdin.readline().split())
s = set([sys.stdin.readline() for _ in range(n)])
cnt = 0

for _ in range(m):
    t = sys.stdin.readline()
    if t in s:
        cnt += 1

print(cnt)