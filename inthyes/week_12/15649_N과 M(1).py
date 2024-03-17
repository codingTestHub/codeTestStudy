from itertools import permutations
n, m = map(int, input().split())
# p = permutations(range(1, n+1), m)
# for i in p:
#     print(" ".join(map(str, i)))

li = []
def back():
    if len(li) == m:
        print(" ".join(map(str, li)))
        return
    for i in range(1, n+1):
        if i not in li:
            li.append(i)
            back()
            li.pop()

back()