import sys
input = sys.stdin.readline

n = int(input())  # 가지고 있는 숫자 카드 개수
n_list = list(map(int, input().split()))  # 숫자 카드에 적혀있는 정수
m = int(input())  # 비교할 정수의 개수
m_list = list(map(int, input().split()))  # 비교해야 할 숫자

# 각 숫자의 개수를 저장할 딕셔너리
cnt = {}

# n_list에서 각 숫자의 개수 세기
for i in n_list:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

# m_list에서 각 숫자의 개수 출력
for i in m_list:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')