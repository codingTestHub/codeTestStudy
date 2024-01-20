# 시간초과 이슈
import sys   # 이걸로 시간초과 해결
# input() 이 sys.stdin.readline() 보다 느린 이유 :
# input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고,
# 개행 문자를 삭제한 값을 리턴하기 때문에 느리다.

# 반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않습니다.

n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

n_list.sort()

for i in n_list:
    print(i)