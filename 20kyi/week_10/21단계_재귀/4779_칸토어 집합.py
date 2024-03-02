# 칸토어 집합은 0과 1사이의 실수로 이루어진 집합

# 3등분 분할 정복
def cantorian(n):
    if n == 1:      # 분할 정복이 계속되어 n의 길이가 1이 되었을 때
        return "-"  # "-" 하나를 리턴하고 함수 종료
    side = cantorian(n//3)  # 왼,오른쪽을 분할 정복하고,
    mid = " " * (n//3)      # 가운데는 빈칸으로 만들어줌
    return side + mid + side

# 입력 받기
while 1:
    try:
        n = int(input())
        result = cantorian(3**n)    #3의 n제곱
        print(result)
    except:
        break
