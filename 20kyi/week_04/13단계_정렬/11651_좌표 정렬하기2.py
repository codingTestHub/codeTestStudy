# 방법1
import sys
input = sys.stdin.readline

n = int(input())
n_list = []

for i in range(n):
    x, y = map(int, input().split())
    n_list.append([y, x])   # y 기준으로 정렬

n_list.sort()

for y, x in n_list:
    print(x, y)


# 방법2
# import sys
#
# n = int(sys.stdin.readline())
# n_list = []
#
# for i in range(n):
#     n_list.append(list(map(int, sys.stdin.readline().split())))
#
# n_list.sort(key=lambda x:(x[1],x[0]))
#
# for i in n_list:
#     print(n_list[i][0], n_list[i][1])
