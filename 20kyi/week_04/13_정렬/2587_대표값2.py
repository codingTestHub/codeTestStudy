n_list = []

for i in range(5):
    n_list.append(int(input()))

n_list = sorted(n_list)

avg = sum(n_list) / len(n_list)     # 평균
mid = len(n_list)//2                # 중앙값

print(int(avg))
print(n_list[mid])