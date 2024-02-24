n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

answer = 0
def dfs(x, y):
    if graph[x][y] == '|':
        graph[x][y] = 'o'

        for _x in [1, -1]:
            X = x + _x
            if (X > 0 and X < n) and graph[X][y] == '|':
                dfs(X, y)
    if graph[x][y] == '-':
        graph[x][y] = 'o'

        for _y in [1, -1]:
            Y = y + _y
            if (Y > 0 and Y < m) and graph[x][Y] == '-':
                dfs(x, Y)

for i in range(n):
    for j in range(m):
        if graph[i][j] == '|' or graph[i][j] == '-':
            dfs(i, j)
            answer += 1
print(answer)