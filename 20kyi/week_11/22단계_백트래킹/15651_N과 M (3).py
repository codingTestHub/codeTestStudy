import sys

input = sys.stdin.readline

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
n, m = list(map(int, input().split()))
s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        # if i not in s:    # 중복허용되므로 삭제
        s.append(i)
        dfs()
        s.pop()


dfs()
