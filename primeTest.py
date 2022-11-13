num = int(input('Provide a number to test:\n'))

prime = True

for i in range(2,num):
    if num%i ==0:
        prime=False
        break
    
if prime==True:
    print('{} is prime'.format(num))
else:
    print('{} is not prime'.format(num))