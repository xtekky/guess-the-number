from random import randrange
from time import sleep

num = randrange(1,100,1)
print(num)
print('I picked a number between 1 and 100 and you have to guess it!')
sleep(2)

guess = int(input('Take your guess: '))
ess = 1

def loop():
    global guess
    global ess
    if guess > num:
        print('')
        print('The guessed number is smaller!')
        guess = int(input('Guess again: '))
        ess = ess+1
    if guess < num:
        print('')
        print('The guessed number is larger!')
        guess = int(input('Guess again: '))
        ess = ess + 1
    if guess == num:
        if ess == 1:
            print('First Try!')
            exit()
        else:
            print(' Lesgoo, you guessed it right, it was:', num, ', and it took you',ess,'guesses!' )
            exit()

while True:
    loop()

