# ???

# 방법1 - 메모리 초과로 실패
# for문 속에서 append를 사용하게 되면 메모리 재할당이 이루어져서 메모리를 효율적으로 사용못한다.
# import sys
# n = int(input())
# n_list = []
# for _ in range(n):
#     n_list.append(int(sys.stdin.readline()))
#
# n_list.sort()
# for i in n_list:
#     print(i)

# 방법2 - 공간복잡도 줄이기
import sys

n = int(sys.stdin.readline())
n_list = [0] * 10001  # 입력값이 10000개 까지 주어질 수 있으니 10000개 만큼의 리스트를 만들어 놓는다

for _ in range(n):
    n_list[int(sys.stdin.readline())] += 1  # 리스트에 각 요소마다 0을 할당해놓고 입력값을 받을 때마다 그 입력값과 같은 인덱스에 +1씩 해준다.

for i in range(10001):
    if n_list[i] != 0:  # 0보다 큰 요소를 갖는 인덱스들을 찾아서 그 수만큼 인덱스를 출력
        for j in range(n_list[i]):
            print(i)
