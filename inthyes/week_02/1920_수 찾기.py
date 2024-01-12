n = int(input())
nli = set(list(map(int,input().split())))
m = int(input())
mli = list(map(int,input().split()))

for i in mli:
    if i in nli:
        print(1)
    else:
        print(0)

