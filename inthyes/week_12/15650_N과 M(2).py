def back(s):
    if len(li) == m:
        print(" ".join(map(str, li)))
        return
    for i in range(s, n+1):
        if i not in li:
            li.append(i)
            back(i+1)
            li.pop()

n, m = map(int, input().split())
li = []
back(1)
