# ???

import sys
from collections import deque

input = sys.stdin.readline
deque = deque()

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = int(input())
c = list(map(int, input().split()))

for i in range(n):
    if a[i] == 0:
        deque.append(b[i])      # b[i] 값을 deque에 추가

for i in c:
    deque.appendleft(i)     # 각각의 값을 deque 왼쪽에 추가
    print(deque.pop(), end=' ')     # 오른쪽 끝 값 꺼내 출력 후 공백 추가
