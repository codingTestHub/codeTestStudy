# ???

# 규칙1 : 밑으로 내려오는 화살표는 짝수
# 규칙2 : 위로 올라가는 화살표는 홀수
# 규칙3 : 짝수 라인은 분자가 증가하고 분모가 감소한다.
# 규칙4 : 홀수 라인은 분자가 감소하고 분모가 증가한다.

X = int(input())
line = 1

# 몇번째 줄에 몇번째 위치의 분수 찾기
while X > line:
    X -= line
    line += 1

# 짝수일 경우
if line % 2 == 0:
    a = X  # 분모
    b = line - X + 1  # 분자

# 홀수일 경우
elif line % 2 != 0:
    a = line - X + 1  # 분모
    b = X  # 분자

print(a, '/', b, sep="")
