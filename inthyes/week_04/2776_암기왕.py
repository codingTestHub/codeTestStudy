t = int(input())
for _ in range(t):
    n = int(input())
    li = set(sorted(map(int, input().split())))
    m = int(input())
    li2 = list(map(int, input().split()))
    # print(li2)

    for i in li2:
        if i in li:
            print(1)
        else:
            print(0)
