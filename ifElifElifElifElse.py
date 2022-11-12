name = input('What is your name?\n')

if name== 'Bob':
    print('Hey {} how are you doing?'.format(name))
elif name == 'Alice':
    print('Hey {} nice to see you'.format(name))
elif name == 'Sally':
    print('Hey {} happy birthday!!'.format(name))
else:
    print('I dont know you {}, go away!'.format(name))