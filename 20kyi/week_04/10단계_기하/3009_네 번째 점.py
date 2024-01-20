# 세 점이 주어졌을 때,
# 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# x좌표와 y좌표를 따로 리스트에 저장한 후, 혼자 다른 값만 출력하면 결과값임

X = []
Y = []

for _ in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(3):
    if X.count(X[i]) == 1:
        x4 = X[i]
    if Y.count(Y[i]) == 1:
        y4 = Y[i]

print(x4, y4)
