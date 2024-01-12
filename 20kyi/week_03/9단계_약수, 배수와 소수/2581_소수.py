# ???

# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

M = int(input())
N = int(input())
arr = []    # 소수 리스트

for i in range(M, N + 1):
    if i == 1:      # 1은 제외
        pass
    elif i == 2:    # 2는 소수 중 짝수이면서 소수인 수
        arr.append(i)
    else:
        for j in range(2, i):       # j를 2부터 i-1까지의 숫자로 반복
            if i % j == 0:
                break
            elif j == i - 1:        # i가 2부터 i-1까지의 모든 숫자로 나누어 떨어지지 않았다면 => 소수
                arr.append(i)

if len(arr) == 0:   # 소수가 없을 경우
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
