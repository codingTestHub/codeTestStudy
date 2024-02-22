# ???
import sys
input = sys.stdin.readline

n = int(input())
users = {"ChongChong"}      # 춤을 추고 있는 사람

for i in range(n):
    a, b = input().split()
    if a in users:          # a가 춤을 추는 사람일 경우
        users.add(b)        # 춤을 추는 사람에 b 추가 (a가 b를 춤추게 만듦)
    if b in users:          # b가 춤을 추는 사람일 경우
        users.add(a)        # 춤을 추는 사람에 a 추가 (b가 a를 춤추게 만듦)

print(len(users))