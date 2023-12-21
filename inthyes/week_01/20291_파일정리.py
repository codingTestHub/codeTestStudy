import sys
sys.stdin.readline
n = int(sys.stdin.readline().strip())
ans = {}
for i in range(n):
  i = sys.stdin.readline().split('.')[1].strip()
  if i not in ans:
    ans[i] = 1
  else:
    ans[i] += 1

res = list(ans.keys())
res.sort()
for j in res:
  print(j, ans[j])