import random
secretNumber = random.randint(1,20)

print('I am thinking of a number between 1 and 20')

for guesses in range(1,7):
    guess = int(input('Take a guess\n'))

    if guess<secretNumber:
        print('your guess is too low\n')

    elif guess>secretNumber:
        print("your guess is too high\n")

    #else:
        #break

    if guess==secretNumber:
        print('Congrats, you guessed the number in '+str(guesses)+' guesses\n')
        break

    else:
        print('No, Number of tries ='+str(guesses)+'\n')
