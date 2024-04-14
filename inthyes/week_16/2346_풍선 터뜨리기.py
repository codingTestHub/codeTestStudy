import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque(enumerate(map(int, input().split())))
ans = []
while queue:
    x, y = queue.popleft()
    ans.append(x+1)

    if y > 0:
        queue.rotate(-(y-1))
    elif y < 0:
        queue.rotate(-y)

print(' '.join(map(str, ans)))
