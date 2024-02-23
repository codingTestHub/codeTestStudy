import sys

input = sys.stdin.readline

n = int(input())
n_list = []

for i in range(n):
    n_list.append(int(input()))

n_list.sort()

# 1. 산술평균
avg = round(sum(n_list) / len(n_list))
print(avg)
# 2. 중앙값
mid = n_list[len(n_list) // 2]
print(mid)

# 3. 최빈값
dic = dict()

for i in n_list:        # 빈도수 구하기
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

mx = max(dic.values())  # 빈도수 중 최대값
mx_dic = []

for i in dic:
    if mx == dic[i]:  # 최빈값의 key 저장
        mx_dic.append(i)

if len(mx_dic) > 1:  # 최빈값이 여러개
    print(mx_dic[1])
else:
    print(mx_dic[0])

# 4. 범위
print(max(n_list) - min(n_list))
