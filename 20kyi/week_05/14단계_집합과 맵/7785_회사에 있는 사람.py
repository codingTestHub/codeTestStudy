# ???

import sys
n = int(input())
dic = {}

for _ in range(n):
    name, log = sys.stdin.readline().split()
    dic[name] = log     # 키: name, 값: log
    if log == "leave":
        del dic[name]   # 딕셔너리 삭제

dic = sorted(dic.items(), reverse=True)     # 사전 역순으로 정렬
dic = dict(dic)         # 딕셔너리 함수로 딕셔너리 생성

for key in dic.keys():
    print(key)

