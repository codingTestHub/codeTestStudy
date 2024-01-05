# ???
# N: 바구니 개수
# M: 공을 넣는 횟수

N, M = map(int, input().split())    # 바구니 개수 N과 반복 횟수 M 입력
box = [0 for _ in range(N)]         # box라는 list 선언후 0으로 초기화

for _ in range(M):
    # i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다
    i, j, k = map(int, input().split())
    for n in range(i, j + 1):
        box[n-1] = k

for n in range(N):
    print(box[n], end=" ")
