a, b = input().split()

if int(a) >= 1 and int(b) <= 10000:
    sum = int(a) + int(b)
    sub = int(a) - int(b)
    mul = int(a) * int(b)
    div = int(a) / int(b)
    rem = int(a) % int(b)

    print(sum)
    print(sub)
    print(mul)
    print(int(div))
    print(rem)