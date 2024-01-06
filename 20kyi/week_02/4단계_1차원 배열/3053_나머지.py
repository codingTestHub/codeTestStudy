num = []

for i in range(10):
    data = int(input())
    if data % 42 not in num:
        num.append(data % 42)

print(len(num))