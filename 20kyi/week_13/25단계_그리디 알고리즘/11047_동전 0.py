import sys

input = sys.stdin.readline

n, k = map(int, input().split())  # n : 화폐 종류, k : 거슬러 줄 돈
coins = []  # 계산대 안에 있는 화폐 리스트
ans = 0

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

for coin in coins:
    # 거슬러 줄 돈 >= 계산대 안에 있는 화폐
    if k >= coin:
        ans = ans + k // coin  # 몫 만큼 더하기
        k = k % coin  # 나머지 할당
        # 더 이상 나눌 수 없으면 break
        if k <= 0:
            break

print(ans)  # 거슬러 준 동전 + 화폐의 수
