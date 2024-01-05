# ???

S = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
# dial = [0, 1, 2, 3, 4, 5, 6, 7]
time = 0

for i in range(len(S)):     # 입력받은 S의 길이 len() 만큼 i를 반복
    for j in dial:          # dial에 있는 문자열 하나하나를 j로 반복
        if S[i] in j:       # 입력받은 S가 j의 문자열에 해당한다면
            time = time + dial.index(j) + 3     # j가 0부터 반복 시작하므로 +2(+1) => +3

print(time)
