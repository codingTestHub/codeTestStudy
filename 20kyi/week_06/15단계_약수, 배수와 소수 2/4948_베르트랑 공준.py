# ???
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램
# 제한 : 1 ≤ n ≤ 123,456


import sys
import math

input = sys.stdin.readline


def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):  # 2부터 제곱근 까지의 숫자
        if x % i == 0:
            return False
    return True


li = list(range(2, 246912))  # 1 ≤ n ≤ 123,456
prime_li = []
for i in li:
    if primenumber(i):
        prime_li.append(i)

while 1:
    n = int(input())
    cnt = 0
    if n == 0:
        break

    for i in prime_li:
        if n < i <= n * 2:
            cnt += 1

    print(cnt)
