n = int(input())
cnt = 0     # 설탕 봉지의 개수

while n >= 0:
    if n % 5 == 0:      # 설탕을 5kg으로 먼저 나눔
        cnt = cnt + int(n // 5)     # 몫만큼 설탕 봉지의 개수 증가
        print(cnt)
        break
    n = n - 3           # 5의 배수가 될 때 까지 3kg 봉지에 담음
    cnt = cnt + 1       # 3kg 봉지에 담을 때 마다 설탕 봉지의 개수 증가
else:
    print(-1)           # 정확하게 n킬로그램을 만들 수 없다면 -1을 출력
