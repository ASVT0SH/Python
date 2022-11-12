num = int(input('Please provide a number:\n'))
print('here is a times table for {}'.format(num))

for i in range(1,11):
    print('{} X {} = {}'.format(num,i,num*i))
