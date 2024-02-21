# import sys
# sys.setrecursionlimit(10**9)
#
# input = sys.stdin.readline
#
# def dfs(value):
#     global cnt
#     visited[value] = cnt
#
#     for v in graph[value]:
#         if visited[v] == 0:
#             cnt += 1
#             dfs(v)
#
# n, m, r = map(int, input().split())
# cnt = 1
#
# graph = [[] for _ in range(n+1)]
# visited = [0] * (n+1)
#
# for _ in range(m):
#     s, e = map(int, input().split())
#     graph[s].append(e)
#     graph[e].append(s)
#     graph[s].sort()
#
# dfs(r)
#
# for _ in range(1, n+1):
#     print(visited[_])

import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())  # 정점의 수, 간선의 수, 시작 정점
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)  # 방문 순서 저장. 0이면 방문 X

# 간선 정보 입력받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 인접 노드 정렬
for i in range(1, n + 1):
    graph[i].sort()

print(graph)


# DFS 구현
def dfs(graph, start, visited):
    stack = [start]
    c = 1

    while stack:
        print("stack: ", stack)
        v = stack.pop()
        print(v)
        if visited[v] == 0:
            visited[v] = c
            c += 1
            print("c", c)
            stack.extend(reversed(graph[v]))


dfs(graph, r, visited)

# 방문 순서 출력
for i in range(1, n + 1):
    print(visited[i])
