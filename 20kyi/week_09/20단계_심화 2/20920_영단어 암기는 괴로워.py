# ???

# 자주 나오는 단어일수록 앞에 배치한다.
# 해당 단어의 길이가 길수록 앞에 배치한다.
# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
words = {}
for i in range(n):
    word = input().rstrip()

    if len(word) < m:  # 길이가 m 이상인 단어들만 외운다
        continue
    else:
        if word in words:  # 단어가 있는 경우
            words[word] += 1
        else:  # 단어가 없는 경우
            words[word] = 1

words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
# x[0] = 단어, x[1] = 단어 빈도수
# -x[1] = 자주 나오는 단어 앞에 배치
# -len(x[0]) = 단어 길이 길수록 앞에 배치
# x[0] = 단어 사전 순 정렬

for i in words:
    print(i[0])