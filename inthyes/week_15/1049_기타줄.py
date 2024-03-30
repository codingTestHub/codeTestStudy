n, m = map(int, input().split())
package = []
single = []
for _ in range(m):
    x, y = map(int, input().split())
    package.append(x)
    single.append(y)

min_package = min(package)
ans = 0

while n > 0:
    # n이 6보다 클 경우, min_single을 배열의 최소값을 6번 곱한 값으로 설정
    # 6보다 작을 경우, min_single을 배열의 최소값을 n번 곱한 값으로 설정
    if n >= 6:
        min_single = min(single) * 6
        n -= 6
    else:
        min_single = min(single)*n
        n -= n
    if min_single < min_package:
        ans += min_single
    else:
        ans += min_package

print(ans)