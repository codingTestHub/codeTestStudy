# 시간초과...
# import sys
# import math
# input = sys.stdin.readline
#
# n = int(input())
# trees = []
# distance = []
# cnt = 0
#
# # 가로수 좌표 입력
# for i in range(n):
#     trees.append(int(input()))
#
# # 가로수 간의 거리
# for i in range(len(trees) - 1):
#     diff = trees[i] - trees[i - 1]
#     distance.append(diff)
#
# # 최대공약수로 새로 심을 가로수 수 구하기
# for j in distance:
#     cnt += j // math.gcd(*distance) - 1
#
# print(cnt)

# 방법 2
import sys
import math

input = sys.stdin.readline

n = int(input())
trees = [int(input()) for _ in range(n)]

# 차이와 최대공약수 계산
differences = [trees[i] - trees[i - 1] for i in range(1, n)]
gcd_value = math.gcd(*differences)

# 심을 나무 수 계산
cnt = sum(diff // gcd_value - 1 for diff in differences)

print(cnt)
