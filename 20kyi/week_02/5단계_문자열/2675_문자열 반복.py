# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램

T = int(input())  # 테스트 케이스 수

for i in range(T):
    # R : 반복할 횟수
    # S :문자열 입력
    R, S = input().split()
    for j in range(len(S)):
        print(S[j] * int(R), end="")
    print("")  # 줄넘김
