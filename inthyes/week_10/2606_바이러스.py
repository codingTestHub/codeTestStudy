n = int(input())
m = int(input())
v = 1
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = True
    for x in graph[v]:
        if not visited[x]:
            dfs(x)

dfs(v)
print(sum(visited)-1)