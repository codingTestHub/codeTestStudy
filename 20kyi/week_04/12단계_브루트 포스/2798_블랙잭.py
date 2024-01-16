n, m = map(int, input().split())    # 카드의 개수, 카드의 합
card = list(map(int, input().split()))      # 카드 리스트
card_sum = 0                        # 카드 3개의 합

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if card[i] + card[j] + card[k] > m:
                continue
            else:
                card_sum = max(card_sum, card[i] + card[j] + card[k])

print(card_sum)