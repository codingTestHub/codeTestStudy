import sys
n = int(input())
array = sorted(list(map(int, input().split())))
start, end = 0, n-1
minTake = sys.maxsize

while start < end:
    x = array[start] + array[end]
    if abs(x) < minTake:
        minTake = abs(x)
        result = [array[start], array[end]]
    if x < 0:
        start += 1
    elif x > 0:
        end -= 1
    else:
        break

print(result[0], result[1])