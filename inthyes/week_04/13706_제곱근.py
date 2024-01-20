n = int(input())
s = 0
e = n
while s <= e:
    mid = (s + e)//2
    if mid ** 2 == n:
        print(mid)
        break
    elif mid ** 2 > n:
        e = mid - 1
    else:
        s = mid + 1
