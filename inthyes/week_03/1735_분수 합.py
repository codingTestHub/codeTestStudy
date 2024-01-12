def gcd(x,y):
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y

a, b = map(int,input().split())
c, d = map(int, input().split())

x = (a * d) + (b * c)
y = b * d
n = gcd(x,y)
print(x//n, y//n)