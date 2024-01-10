from collections import deque
n, k = map(int,input().split())
res = []
queue = deque([i for i in range(1,n+1)])

while len(queue) > 0:
    queue.rotate(-(k-1))
    res.append(queue.popleft())

print("<", end = "")
for i in res:
    print(i, end = "")
    if i != res[-1]:
        print(", ",end = "")
print(">", end = "")