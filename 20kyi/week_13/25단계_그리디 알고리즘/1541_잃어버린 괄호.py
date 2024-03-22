#  괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
import sys
input = sys.stdin.readline

n = str(input())
m = n.split('-')
ans = 0

x = sum(map(int, (m[0].split('+'))))    # '+'를 기준으로 끊기
if n[0] == '-':
    ans = ans - x
else:
    ans = ans + x

for x in m[1:]: # 첫번째 제외하고 시작
    x = sum(map(int, (x.split('+'))))
    ans = ans - x

print(ans)