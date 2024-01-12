import sys

S = int(input())
for i in range(S):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)