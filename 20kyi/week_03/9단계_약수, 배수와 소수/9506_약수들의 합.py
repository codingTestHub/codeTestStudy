while 1:
    N = int(input())
    if N == -1:
        break
    arr = []
    result = 0

    for i in range(1, N + 1):
        if N % i == 0:
            arr.append(i)

    for i in arr[:-1]:  # 마지막 원소 N 제외
        result += i

    if N == result:
        # print(N, "=", arr[:-1])
        print(f"{N} = {' + '.join(map(str, arr[:-1]))}")
    else:
        print(N, "is NOT perfect.")  # Not으로 오타나서 2번이나 실패;;
