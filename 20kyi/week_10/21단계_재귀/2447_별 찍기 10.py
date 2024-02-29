def print_star(n):
    if n == 1:
        return ["*"]
    stars = print_star(n // 3)
    list = []

    for star in stars:
        list.append(star * 3)
    for star in stars:
        list.append(star + ' ' * (n // 3) + star)
    for star in stars:
        list.append(star * 3)

    return list


n = int(input())    # n은 3의 거듭제곱
print('\n'.join(print_star(n)))
