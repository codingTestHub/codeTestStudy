# 유클리드 호제법
# a * b // (a와 b의 최대공약수)

import sys
import math

a, b = map(int, sys.stdin.readline().split())
print(a * b // math.gcd(a, b))
