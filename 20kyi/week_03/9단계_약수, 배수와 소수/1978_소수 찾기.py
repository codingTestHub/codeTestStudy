N = int(input())    # 테스트 케이스 수
number = list(map(int, input().split()))    # 테스트 케이스
result = 0           # 소수 개수

for num in number:
    cnt = 0     # 나머지가 0인 숫자의 개수

    if num == 1:    # 1 제외
        continue

    for x in range(2, num + 1):     # 1을 제외하고 2부터 시작
        if num % x == 0:            # 나머지가 0일 경우 cnt 증가
            cnt += 1

    if cnt == 1:    # 나머지가 0인 숫자가 1개일 경우 소수이다.
        result += 1

print(result)
