import sys
input = sys.stdin.readline

k = int(input())
k_list = []

for _ in range(k):
    num = int(input())

    if num != 0:
        k_list.append(num)
    else:
        k_list.pop()

print(sum(k_list))