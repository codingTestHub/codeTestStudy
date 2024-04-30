n = int(input())

# 첫번째 문자열을 리스트 형태로 입력받는다
first = list(input())

for i in range(n-1):
    # 첫번째를 제외한 나머지 문자열을 입력받는다
    other = list(input())
    # 첫번째 문자열의 j위치와 다른 문자열의 j위치를 비교한다.
    for j in range(len(first)):
        if first[j] != other[j]:
            first[j] = '?'
print(''.join(first))