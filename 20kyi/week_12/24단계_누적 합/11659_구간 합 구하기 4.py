# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램
# 원본 리스트를 A, 누적 합 리스트를 S라고 할 때,
# 1. 누적 합 구하기: S[i] = S[i-1] + A[i]
# 2. 구간 합 구하기: S[j] - S[i-1]

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = list(map(int, input().split()))    # n개의 수

for i in range(n-1):
    n_list[i+1] += n_list[i]
n_list = [0] + n_list

for _ in range(m):
    i, j = map(int, input().split())
    print(n_list[j]-n_list[i-1])    # 구간 합
