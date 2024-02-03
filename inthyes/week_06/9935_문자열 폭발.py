from sys import stdin

a = stdin.readline().rstrip()
b = stdin.readline().rstrip()

stack = []
b_len = len(b)

#a만큼 반복하면서 stack에 값 삽입
for i in range(len(a)):
    stack.append(a[i])
    if ''.join(stack[-b_len:]) == b:
        for _ in range(b_len):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")