"""This is a lambda function that takes two arguments
 and returns the first argument raised to the power of
  the second argument."""

process = lambda x, y: x**y

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))

print(f"{x} raised to {y} is {process(x, y)}")
