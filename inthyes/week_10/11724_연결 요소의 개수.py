# 재귀 깊이 2500으로 변경
import sys
sys.setrecursionlimit(2500)

# input = sys.stdin.readline
def dfs(v):
    visited[v] = True
    # print(v, end = " ")
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

for x in range(1, n+1):
    if not visited[x]:
        dfs(x)
        cnt += 1
print(cnt)