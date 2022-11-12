sentence = 'Have a nice day'
numbers = [1,2,3,4,5,6,7,8]
letters = ('a','b','c','d')

for c in sentence:
    print(c.upper())

print()

for n in numbers:
    print('Square of {} is {}'.format(n,n**2))

print()

for letter in letters:
    print(letter.center(5,'_'))