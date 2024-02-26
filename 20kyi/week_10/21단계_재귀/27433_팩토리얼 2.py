# 재귀함수 이용한 팩토리얼

import sys
input = sys.stdin.readline

n = int(input())

def factorial(t):
    result = 1
    for i in range(1, t + 1):
        result = result * i
    return result

print(factorial(n))