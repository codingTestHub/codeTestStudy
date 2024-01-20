# 이분탐색
n = int(input())
s = 0 # 시작점 0으로 지정
e = n # 끝점 n으로 지정

while s <= e: # 시작점이 끝점보다 커지면 끝나는 반복문
    mid = (s + e) // 2
    if mid ** 2 < n:
        s = mid + 1
    else:
        e = mid - 1
print(s)
