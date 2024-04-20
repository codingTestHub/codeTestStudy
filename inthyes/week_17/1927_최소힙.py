import sys
import heapq

n = int(input())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    # num == 0인 경우
    else:
        # heapq.heappop(heap)을 시도하고 아닐 경우 0을 출력하도록 예외처리
        try:
            print(heapq.heappop(heap))
        except:
            print(0)