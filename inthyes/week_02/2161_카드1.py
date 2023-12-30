n = int(input())

# 기존 리스트와 새로운 값을 받을 리스트 생성
li = [i for i in range(1, n+1)]
res = []

# 기존 리스트가 1이 될때까지 반복하는 while문 생성
while len(li) != 1:
    res.append(li.pop(0))
    li.append(li.pop(0))


for j in res:
    print(j, end = " ")
print(li[0])
