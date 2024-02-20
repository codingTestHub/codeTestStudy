import sys

input = sys.stdin.readline


def factorial(t):
    result = 1
    for i in range(1, t + 1):
        result = result * i
    return result


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(n) * factorial(m - n)))
