import sys
input = sys.stdin.readline

n, m = map(int,input().split())

A = set()
cnt = 0

for _ in range(n):
    A.add(input().rstrip())

for i in range(m):
    x = input().rstrip()
    if x in A:
        cnt += 1

print(cnt)