import sys
import math

input1 = sys.stdin.readline
a1, b1 = map(int, input1().split())
a2, b2 = map(int, input1().split())

a3 = a1 * b2 + a2 * b1
b3 = b1 * b2

A = (a3 // math.gcd(a3, b3))
B = (b3 // math.gcd(a3, b3))

print(A, B)