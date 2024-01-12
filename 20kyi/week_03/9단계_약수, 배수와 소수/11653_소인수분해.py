N = int(input())  # 정수 입력
i = 2  # 1을 제외한 가장 작은 수 2부터 나누기

while N != 1:
    if N % i == 0:  # N을 0이 될때까지 나눴다면
        print(i)
        N = N / i
    else:
        i += 1  # 0으로 나누어 떨어지지 않았다면 i 증가해서 다시 나누기
