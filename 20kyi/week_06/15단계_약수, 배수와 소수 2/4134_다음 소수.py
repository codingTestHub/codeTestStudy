import sys
import math

input = sys.stdin.readline


# 소수 판별 알고리즘
def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):  # 2부터 제곱근 까지의 숫자
        if x % i == 0:
            return False
    return True


n = int(input())
for i in range(n):
    num = int(input())
    while True:
        if num == 0 or num == 1:
            print(2)
            break
        if primenumber(num):        # 소수일 경우 자기 자신을 출력
            print(num)
            break
        else:                       # 소수가 아닐 경우 소수가 될 때 까지 1 더하기
            num += 1
