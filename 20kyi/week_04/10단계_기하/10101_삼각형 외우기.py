a = int(input())
b = int(input())
c = int(input())

if a and b and c == 60:
    print("Equilateral")
elif (a + b + c == 180) and (a==b or a==c or b==c):
    print("Isosceles")
elif (a + b + c == 180) and (a != b != c):
    print("Scalene")
else:
    print("Error")
