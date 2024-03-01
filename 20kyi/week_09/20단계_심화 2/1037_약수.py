import sys
input = sys.stdin.readline

n = int(input())    # 진짜 약수의 개수
a = list(map(int, input().split()))     # 진짜 약수 리스트

max_a = max(a)
min_a = min(a)

print(max_a * min_a)