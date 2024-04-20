t = int(input())
for tc in range(t):
    n = input().split()
    for i in n:
        print(i[::-1], end = " ")
