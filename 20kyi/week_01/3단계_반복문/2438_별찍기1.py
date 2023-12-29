# T = int(input())
#
# for i in range(T):
#     for j in range(i+1):
#         print("*", end="")
#     print("")


# 2439_별찍기2
T = int(input())

for i in range(1, T + 1):
    print(" " * (T - i) + "*" * i)

# for i in range(T):
#     for j in range(T - i):
#         print(" ", end="")
#     for k in range(i + 1):
#         print("*", end="")
#     print("")
