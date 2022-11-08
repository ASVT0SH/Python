name = 'blackThunder'
password = 'Themepark123'
print('Enter name')
newUName = input()
if newUName == name:
    print('Welcome '+ newUName)
    print('Enter password')
    uPassword = input()
    if uPassword == password :
        print('Access Granted ')
    else:
        print('You are a stranger')
else:
    print('Register yourself')

age = 25
while age < 32:
    print('You are '+ str(age)+' years young')
    age += 1