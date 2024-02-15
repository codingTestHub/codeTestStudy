from collections import deque

n, k = map(int, input().split())
deque = deque([i for i in range(1, n+1)])
res = []    # 결과 배열
while len(deque) != 0:
    for _ in range(k-1):
        deque.append(deque.popleft())   # k-1까지 deque 맨 뒤로 이동
    res.append(str(deque.popleft()))    # k번째 삭제 후 결과 배열에 추가

print('<' + ', '.join(res) + '>')