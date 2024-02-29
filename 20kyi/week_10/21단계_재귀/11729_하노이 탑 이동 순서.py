import sys

input = sys.stdin.readline

n = int(input())


def hanoi_tower(n, a, b, c):    # a-시작, c-도착
    if n == 1:
        print(a, c)
        return

    hanoi_tower(n - 1, a, c, b)
    print(a, c)
    hanoi_tower(n - 1, b, a, c)


k = 2 ** n - 1  # 옮긴 횟수 => 최소한의 이동값
print(k)
hanoi_tower(n, 1, 2, 3)