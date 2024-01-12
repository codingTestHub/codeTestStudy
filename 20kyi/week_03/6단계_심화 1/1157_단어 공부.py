#???

word = input().upper()          # 전체 문자를 대문자로 변환
word_list = list(set(word))     # set 함수를 이용하여 중복 제거
cnt = []                        # 알파벳이 사용된 횟수 저장 리스트

for i in word_list:
    count = word.count          # 알파벳 사용된 횟수 카운트
    cnt.append(count(i))        # 알파벳 사용 횟수를 cnt에 저장

if cnt.count(max(cnt)) > 1:     # cnt 최대값이 2개 이상일 경우 물음표 출력
    print("?")
else:
    max_index = cnt.index((max(cnt)))   # cnt 숫자 최대값 인덱스(위치)
    print(word_list[max_index])

