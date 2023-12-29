# list를 사용할 경우 시간초과 발생, set으로 입력받은 후 교집합 출력
n, m = map(int,input().split())

a = set()
for _ in range(n):
    a.add(input())

b = set()
for _ in range(m):
    b.add(input())

li = sorted(list(a&b))

print(len(li))

for i in li:
    print(i)