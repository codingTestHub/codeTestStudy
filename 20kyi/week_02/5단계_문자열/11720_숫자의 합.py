# sum 함수
N = input()
print(sum(map(int, input())))

# for문
N = input()         # 입력할 숫자의 개수
nums = input()      # 입력할 숫자
total = 0

for i in nums:
    total = total + int(i)

print(total)
