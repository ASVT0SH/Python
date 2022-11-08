print('Hello world')
print('Enter name')
name=input()

print('Hi '+name)
print('Enter age')
age = input()

print('you will be '+str(int(age)+1)+' years next year')

if int(age)<=18 :
    print('not eligible')
elif int(age)>18 and int(age)<=25 :
    print('Eligible for DL')
elif int(age)>25 and int(age)<=35 :
    print('eligible for marriage')
else :
    print('Too old')

