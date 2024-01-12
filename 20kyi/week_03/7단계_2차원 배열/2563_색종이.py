# ???

n = int(input())      # 색종이의 수
arr = [[0 for _ in range(101)] for _ in range(101)]     # 2차원 배열 선언 => 100x100 도화지

for _ in range(n):
    x, y = list(map(int, input().split()))      # 색종이를 붙일 위치(x, y)
    for row in range(x, x+10):
        for col in range(y, y+10):
            arr[row][col] = 1
result = 0

for i in arr:       # 색종이를 붙인 위치를 1로 카운팅
    result = result + sum(i)

print(result)
