import sys
input = sys.stdin.readline

n = int(input())
peoples = list(map(int, input().split()))   # 기다리는 사람들 리스트

peoples.sort()

ans = 0

for i in range(1, n+1):
    ans = ans + sum(peoples[0:i])

print(ans)