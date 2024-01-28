import sys

n = int(input())  # 가지고 있는 숫자 카드 개수
n_list = list(map(int, sys.stdin.readline().split()))  # 숫자 카드에 적혀있는 정수
m = int(input())  # 비교할 정수의 개수
m_list = list(map(int, sys.stdin.readline().split()))  # 비교해야 할 숫자

n_list.sort()  # 이분 탐색을 위해 먼저 정렬해야 함!!


# 이분 탐색 사용
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:  # 이분탐색하여 비교 값과 중간 값이 같다면 중간값 리턴
            return mid
        elif array[mid] > target:  # 이분탐색하여 비교 값이 중간 값의 왼쪽에 있다면 중간값 왼쪽으로
            end = mid - 1
        else:  # 이분탐색하여 비교 값이 중간 값의 오른쪽에 있다면 중간값 오른쪽으로
            start = mid + 1
    return None


for i in range(m):
    if binary_search(n_list, m_list[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
