# ???

import sys
S = sys.stdin.readline().strip()
result = set()      # 결과 문자열 중복 제거

for i in range(len(S)):
    for j in range(i, len(S)):
        result.add(S[i:j+1])    # S의 i번째 문자부터 j번째 문자까지 부분 문자열

print(len(result))