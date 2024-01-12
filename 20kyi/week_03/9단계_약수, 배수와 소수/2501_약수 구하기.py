N, K = map(int, input().split())  # 자연수, K번째 작은 약수
arr = []

for i in range(1, N + 1):
    if N % i == 0:
        arr.append(i)

if K <= len(arr):
    print(arr[K-1])
else:       # N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우
    print(0)
