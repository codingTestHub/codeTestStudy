# ???

n, m = map(int, input().split())
board = []  # 전체 체스판
result = []  # 결과 체스판

for i in range(n):
    board.append(input())

# 8X8로 자르기
for x in range(n - 7):
    for y in range(m - 7):
        w_index = 0  # 흰색으로 시작
        b_index = 0  # 검은색으로 시작
        for i in range(x, x + 8):
            for j in range(y, y + 8):
                if (i + j) % 2 == 0:  # 짝수인 경우
                    if board[i][j] != 'W':
                        w_index += 1
                    else:
                        b_index += 1
                else:  # 홀수인 경우
                    if board[i][j] != "W":
                        b_index += 1
                    else:
                        w_index += 1
        result.append(w_index)
        result.append(b_index)
print(min(result))
