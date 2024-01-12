# word = []
# for i in range(5):
#     a = input()
#     word.append(a)

word = [input() for i in range(5)]

for j in range(15):         # 단어의 최대 길이는 15
    for i in range(5):      # 총 다섯 줄의 입력
        if j < len(word[i]):    # j가 단어 길이보다 작으면 출력
            print(word[i][j], end="")
