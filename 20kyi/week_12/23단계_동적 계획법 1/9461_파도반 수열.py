import sys

input = sys.stdin.readline

dp = [0 for i in range(101)]
dp[1], dp[2], dp[3] = 1, 1, 1  # 초기값이 1인 정수의 나열

for i in range(4, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

T = int(input())  # 테스트 케이스 수

for i in range(T):
    n = int(input())
    print(dp[n])
