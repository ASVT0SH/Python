print('Enter a number')
number = int(input())

#candidate will change in the while loop
#candidate is a potential factor
candidate=1

while candidate <= number:
    if number % candidate ==0:
        print('{} is a factor of {}'.format(candidate,number))
    candidate += 1