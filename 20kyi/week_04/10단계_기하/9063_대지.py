N = int(input())    # 구슬의 개수
X = []
Y = []

for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

x0 = min(X)
y0 = min(Y)

x1 = max(X)
y1 = max(Y)

result = (x1 - x0) * (y1 - y0)
print(result)