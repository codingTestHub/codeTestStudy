from sys import stdin

n, m = map(int, stdin.readline().split())
j = int(stdin.readline())

start = 1
end = m
dis = 0

# j만큼 반복
for _ in range(j):
    P = int(input())

    if P > end:
        dis += (P - end)
        end = P
        start = end - m + 1
    elif P < start:
        dis += (start - P)
        start = P
        end = P + m - 1
print(dis)