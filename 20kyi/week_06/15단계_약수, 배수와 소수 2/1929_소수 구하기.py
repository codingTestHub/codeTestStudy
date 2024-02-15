import sys
import math

input = sys.stdin.readline


# 소수 판별 알고리즘
def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):  # 2부터 제곱근 까지의 숫자
        if x % i == 0:
            return False
    return True


m, n = map(int, input().split())
for i in range(m, n + 1):
    if i == 1:
        continue
    if primenumber(i):
        print(i)
