n = int(input())
ans = []
for _ in range(n):
    ans.append(int(input()))
dic = {}
li = []
for i in ans:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
m = max(dic.values())
for key, value in dic.items():
    if value == m:
        li.append(key)
print(round(sum(ans)/n))
print(sorted(ans)[n//2])
# print(dic)
if len(li) > 1:
    print(sorted(li)[1])
else:
    print(sorted(li)[0])
print((sorted(ans)[-1])-sorted(ans)[0])
