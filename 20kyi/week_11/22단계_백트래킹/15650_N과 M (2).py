import sys

input = sys.stdin.readline

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
n, m = list(map(int, input().split()))
s = []


def dfs(start): # 중복 제거를 위해 start 변수 추가
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()


dfs(1)
