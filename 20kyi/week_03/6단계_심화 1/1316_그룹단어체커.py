# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

N = int(input())    # 입력 받을 단어의 개수
cnt = N             # 그룹 단어 개수 => 총 단어 개수로 초기화

for i in range(N):
    word = input()

    # 단어 한글자씩 탐색
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:     # 비교중인 글자가 그 다음글자 이후에 또 존재할 경우 => 그룹단어 아님
            cnt -= 1
            break

print(cnt)
