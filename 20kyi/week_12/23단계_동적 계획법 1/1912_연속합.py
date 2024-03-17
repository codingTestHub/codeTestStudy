# 연속된 몇 개의 수를 선택해서 가장 큰 합
import sys

input = sys.stdin.readline

n = int(input())
dp = list(map(int, input().split()))

for i in range(1, n):
    dp[i] = max(dp[i], dp[i] + dp[i-1])

print(max(dp))
