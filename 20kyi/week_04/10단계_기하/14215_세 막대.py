a, b, c = map(int, input().split())
sides = sorted([a, b, c])

if sides[0] + sides[1] <= sides[2]:
    # num1 = sides[2] - (sides[1] + sides[0]) + 1
    # num2 = sum(sides) - num1
    # print(num2)
    result = 2*(sides[0] + sides[1]) - 1
    print(result)
else:
    print(a + b + c)
