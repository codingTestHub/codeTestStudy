# ???

import sys

input = sys.stdin.readline


def merge_sort(n):  # A[p..r]을 오름차순 정렬한다.
    if len(n) == 1:
        return n

    mid = (len(n)+1) // 2  # q는 p, r의 중간 지점
    left = merge_sort(n[:mid])  # 전반부 정렬
    right = merge_sort(n[mid:])  # 후반부 정렬
    n2, i, j = [], 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            n2.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            n2.append(right[j])
            ans.append(right[j])
            j += 1

    while i < len(left):
        n2.append(left[i])
        ans.append(left[i])
        i += 1

    while j < len(right):
        n2.append(right[j])
        ans.append(right[j])
        j += 1

    return n2


n, k = map(int, input().split())    # n개, k번째 저장되는 수
A = list(map(int, input().split())) # n개의 정수가 저장된 배열 A
ans = []
merge_sort(A)

if len(ans) >= k:
    print(ans[k - 1])
else:
    print(-1)
