from itertools import permutations
n = int(input())
k = int(input())
res = set()
li = []
for i in range(n):
    li.append(input())

for j in permutations(li, k):
    res.add(''.join(j))

print(len(res))