from itertools import permutations
n = int(input())
k = int(input())
li = []
ans = set()
for _ in range(n):
    li.append(int(input()))

for i in permutations(li, k):
    if k == 2:
        ans.add(str(i[0])+ str(i[1]))
    elif k == 3:
        ans.add(str(i[0])+ str(i[1])+ str(i[2]))
    elif k == 4:
        ans.add(str(i[0]) + str(i[1]) + str(i[2])+ str(i[3]))

print(len(ans))
