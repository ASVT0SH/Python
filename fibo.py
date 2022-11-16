def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

num = int(input("Enter number: "))

for x in range(0,num):
    print(fibonacci(x))