side1 = int(input("Enter length of side 1\n"))
side2 = int(input("Enter length of side 2\n"))
side3 = int(input("Enter length of side 3\n"))

if side1==side2==side3:
    print("Equilateral")
elif side1==side2!=side3 or side1!=side2==side3 or side1==side3!=side2:
    print("Isosceles")
else:
    print("Scalene")