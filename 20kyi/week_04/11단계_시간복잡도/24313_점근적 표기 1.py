# ???
# 첫째 줄에 함수 f(n)을 나타내는 정수 a1, a0가 주어진다. (0 ≤ |ai| ≤ 100)
# 다음 줄에 양의 정수 c가 주어진다. (1 ≤ c ≤ 100)
# 다음 줄에 양의 정수 n0가 주어진다. (1 ≤ n0 ≤ 100)

# f(n) = a1*n + a0, g(n) = n
# 판별식 f(n) ≤ c × g(n)
# a1*n + a0 <= c*n
# (a1-c)*n0 + a0 <= 0 에서 기울기가 양수일 경우 성립하지 않기 때문에 a1-c <= 0 조건 필요

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if (a1 * n0 + a0 <= c * n0) and (a1 - c <= 0):
    print(1)
else:
    print(0)
