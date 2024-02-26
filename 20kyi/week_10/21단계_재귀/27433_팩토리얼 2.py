# 재귀함수 이용한 팩토리얼

import sys

input = sys.stdin.readline

n = int(input())


def factorial(t):
    result = 1
    for i in range(1, t + 1):
        result = result * i
    return result


# 또는
# def factorial(n):
# if(n > 1):
#     return n * factorial(n - 1)
# else:
#     return 1

print(factorial(n))
