n, m = map(int, input().split())
box = [i for i in range(1, n + 1)]  # box라는 list에 1부터 n까지의 숫자 입력
temp = 0  # 바꾸기 위해 temp 변수 선언

for i in range(m):  # m번 동안 바꿀 바구니 i와 j
    i, j = map(int, input().split())
    temp = box[i - 1]  # temp에 i번째 바구니를
    box[i - 1] = box[j - 1]  # i번째 바구니를 j번째 바구니에
    box[j - 1] = temp  # j번째 바구니에 temp를

    # 또는 파이썬에서만 가능한 방법 사용
    # box[i-1], box[j-1] = box[j-1], box[i-1]

for i in range(n):
    print(box[i], end=" ")
