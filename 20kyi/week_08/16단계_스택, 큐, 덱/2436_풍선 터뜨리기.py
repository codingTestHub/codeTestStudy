# ???

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deque = deque(enumerate(map(int, input().split())))
result = []

# enumerate 사용 전
# deque([3, 2, 1, -3, -1])
# enumerate 사용 후
# deque([(0, 3), (1, 2), (2, 1), (3, -3), (4, -1)])

while deque:
    idx, paper = deque.popleft()
    result.append(idx + 1)

    if paper > 0:
        deque.rotate(-(paper - 1))
    elif paper < 0:
        deque.rotate(-paper)

    # tate(-1)은 원형 큐를 반시계방향으로 1칸 회전시키고,
    # rotate(1)은 시계방향으로 1칸 회전시킨다

print(' '.join(map(str, result)))
