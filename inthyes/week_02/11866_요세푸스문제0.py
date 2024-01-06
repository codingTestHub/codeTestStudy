from collections import deque
n, k = map(int,input().split())
deq = deque([i for i in range(1, n+1)])

res = []
while len(deq) != 0:
    for i in range(k-1):
        deq.rotate(-1)
    res.append(deq[0])
    deq.popleft()

print("<", end = "")
for i in range(len(res)):
    print("{}".format(res[i]), end = "")
    if i != len(res)-1:
        print(",", end = " ")
print(">")