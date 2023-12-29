n = int(input())
li = []

for _ in range(n):
    li.append(int(input()))

last = li[-1]
cnt = 1
for i in reversed(range(n)):
    if li[i] > last:
        cnt += 1
        last = li[i]

print(cnt)

