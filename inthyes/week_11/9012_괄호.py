for _ in range(int(input())):
    stack = []
    x = input()
    right, left = 0, 0

    for i in x:
        stack.append(i)
        if i == '(':
            right += 1
        else:
            left += 1

        if right < left:
            break

    if len(x) % 2 == 0 and right == left:
        print("YES")
    else:
        print("NO")