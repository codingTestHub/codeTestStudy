D = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

A = input()
RES = 0
for i in range(len(A)):
    for j in D:
        if A[i] in j:
            RES += D.index(j) + 3
print(RES)