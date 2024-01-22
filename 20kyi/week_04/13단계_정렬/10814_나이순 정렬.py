import sys

n = int(sys.stdin.readline())
n_list = []

for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    n_list.append([age, name])

# n_list.sort()                       # 오답
n_list.sort(key=lambda x: x[0])       # age만 비교

for i in n_list:
    print(i[0], i[1])
