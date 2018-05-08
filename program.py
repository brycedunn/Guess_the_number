# 8 May 2018
""" This program will be a game for a user to guess a random integer between 0 and 100."""
import random
print('------------------------')
print('    GUESS THE NUMBER')
print('------------------------')
player_name = input('What is your name? ')
the_number = random.randint(0,100)
guess = -1
while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Too low, {}.'.format(player_name))
    elif guess > the_number:
        print('Too high, {}.'.format(player_name))
    else:
        print('You win, {}!'.format(player_name))
        break

print('Done!')
