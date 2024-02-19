n, k = map(int, input().split())


def factorial(t):
    result = 1
    for i in range(1, t + 1):
        result = result * i
    return result


res = factorial(n) // factorial(k) // factorial(n-k)
print(res)