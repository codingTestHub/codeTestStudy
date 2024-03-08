# ???
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
# 퀸을 놓지 못하는 경우는 2가지
# 1. 같은 열에 다른 퀸이 있는 경우
# 2. 왼쪽 대각선, 오른쪽 대각선에 다른 퀸이 있는 경우

import sys

input = sys.stdin.readline

n = int(input())

ans = 0
row = [0] * n


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[x] = i  # [x, i]에 퀸을 놓겠다.
            if is_promising(x):
                n_queens(x + 1)


n_queens(0)
print(ans)
