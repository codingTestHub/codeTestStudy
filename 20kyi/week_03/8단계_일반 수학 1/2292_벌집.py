# 1번 시작
# line2 : 2, 3, 4, 5, 6, 7
# line3 : 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
# ...
# (6*0) + (6*1) + (6*2) + ... => 등차수열

N = int(input())
room = 1
cnt = 1

while N > room:
    room += 6 * cnt
    cnt += 1

print(cnt)