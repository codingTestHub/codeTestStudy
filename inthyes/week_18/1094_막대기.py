X = int(input())

Cnt = 0
Len = 0
smallest = 64

# 나무 총 합의 길이가 x와 동일하지 않을 동안 반복한다.
while Len != X:
    # x - len이 가장 짧은 나무일 경우 길이에 가장 짧은 나무의 길이를 더한다.
    if X - Len >= smallest:
        Len += smallest
        Cnt += 1
    # 반복하는 동안 계획 가장 짧은 나무의 길이를 나누기 2로 자른다.
    smallest /= 2
print(Cnt)