# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
# 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
# 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다.
# N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

A, B = [], []       # 행렬A, 행렬B
N, M = map(int, input().split())    # 행렬의 크기 입력

# 행렬 A 입력
for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

# 행렬 B 입력
for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# 행렬 A+B 출력
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=" ")
    print()