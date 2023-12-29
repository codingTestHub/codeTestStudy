# H, M = input().split()
#
# if int(H) == 0:
#     H = 23
# else:
#     H = int(H) - 1
#
# if int(M) < 45:
#     M = int(M) + 15
# else:
#     M = int(M) - 45
#
# print(H, M)

H, M = map(int, input().split())

if M < 45:
    M += 15
    if H == 0:
        H = 23
    else:
        H -= 1
else:
    M -= 45

print(H, M)

