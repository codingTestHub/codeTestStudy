n = int(input())

cnt = 0
while True:
    # 5로 나누어 떨어지지 않을 경우 n-2를 실행하는 조건문 수행
    if n % 5 == 0:
        cnt += n // 5
        break
    else:
        n -= 2
        cnt += 1

    # n이 음수일 경우 while 반복문 종료
    if n < 0:
        break

if n < 0:
    print(-1)
else:
    print(cnt)

