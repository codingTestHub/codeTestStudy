A = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 7:0, 8:0}
B = {6:0, 9:0}
n = str(input())

for i in n:
    if int(i) in A:
        A[int(i)] += 1
    elif int(i) in B:
        B[int(i)] += 1

if sum(B.values()) % 2 != 0:
    x = sum(B.values()) + 1
else:
    x = sum(B.values())

if max(A.values()) >= x//2:
    print(max(A.values()))
else:
    print(x//2)