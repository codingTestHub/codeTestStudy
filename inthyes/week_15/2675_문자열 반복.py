t = int(input())
for tc in range(t):
    n, m = input().split()
    for x in m:
        print(x * int(n), end ="")
    print()