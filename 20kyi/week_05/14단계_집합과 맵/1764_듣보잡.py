import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = []
m_list = []

for i in range(n):
    n_name = input()
    n_list.append(n_name)

for i in range(m):
    m_name = input()
    m_list.append(m_name)

result = list(set(n_list) & set(m_list))    # set 중복제거, & 교집합 추출
result.sort()

print(len(result))
print(''.join(result), end='')
