import sys
input = sys.stdin.readline
n = int(input())
dic = {}
li = []
for i in range(n):
    log = input().split()
    if log[1] not in dic:
        dic[log[0]] = log[1]
    else:
        dic[log[1]] = log[1]

for a, b in dic.items():
    if b == 'enter':
        li.append(a)

for i in sorted(li, reverse= True):
    print(i)
