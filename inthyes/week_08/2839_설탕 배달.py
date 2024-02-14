n = int(input())

x = 0

# n이 0보다 작을 경우 멈추는 반복문
while n >= 0:
    # n이 5로 나누어떨어지는 값일 때
    if n % 5 == 0:
        x += (n // 5)
        print(x)
        break
    # 아닐 경우 n을 3만큼 줄이고 x의 값을 1만큼 키움
    n -= 3
    x += 1
else:
    print(-1)