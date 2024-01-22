import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = []

# a,b에 해당하는 포인터 생성
ap, bp = 0, 0
al, bl = len(A), len(B)

# ap, bp가 해당 리스트 길이와 같아지지 않을동안 반복
while ap != al or bp != bl:
    if ap == al:
        res.append(B[bp])
        bp += 1
    elif bp == bl:
        res.append(A[ap])
        ap += 1
    else:
        if A[ap] < B[bp]:
            res.append(A[ap])
            ap += 1
        else:
            res.append(B[bp])
            bp += 1
print(*res)
