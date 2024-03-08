import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

max_num = -int(1e9)
min_num = int(1e9)


def dfs(depth, total, add, sub, mul, div):
    global max_num, min_num
    if depth == n:
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        return

    if add:
        dfs(depth + 1, total + num[depth], add - 1, sub, mul, div)
    if sub:
        dfs(depth + 1, total - num[depth], add, sub - 1, mul, div)
    if mul:
        dfs(depth + 1, total * num[depth], add, sub, mul - 1, div)
    if div:
        dfs(depth + 1, int(total / num[depth]), add, sub, mul, div - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(max_num)
print(min_num)
