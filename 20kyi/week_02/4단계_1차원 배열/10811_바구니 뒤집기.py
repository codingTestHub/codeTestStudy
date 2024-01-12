N, M = map(int, input().split())
box = [i for i in range(1, N+1)]
temp = 0

for x in range(M):
    i, j = map(int, input().split())
    temp = box[i-1:j]
    temp.reverse()
    box[i-1:j] = temp

for x in range(N):
    print(box[x], end=" ")