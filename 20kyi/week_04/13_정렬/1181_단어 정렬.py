import sys

n = int(sys.stdin.readline())
n_list = []

for i in range(n):
    n_list.append(sys.stdin.readline().strip())     # \n 제거하는 strip

set_list = set(n_list)      # 중복 제거 - set으로 변환
n_list = list(set_list)     # 다시 list로 변환

n_list.sort()               # 사전순 정렬
n_list.sort(key=len)        # 길이순 정렬

for i in n_list:
    print(i)
