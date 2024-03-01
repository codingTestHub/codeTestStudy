import sys
input = sys.stdin.readline

n = int(input())
users = set()
result = 0

for i in range(n):
    user = input().rstrip()
    if user == "ENTER":
        users = set()
    elif user not in users:
        result += 1
        users.add(user)

print(result)
