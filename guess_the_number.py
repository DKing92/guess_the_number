#Beginner projects - Guess the Number

import random

max = 50

def guessing() :
    playing = True
    guesses = 0 
    num = random.randrange(max)   
    
    while playing :
        try :
            guess = input('Guess a number between 0 and 50: ')
            guess_int = int(guess)
        except :
            print('Please enter a valid number') 
            continue
    
        if (guess_int == num) :
            guesses = guesses + 1
            print('You guessed right!\nIt took you ' + str(guesses) + ' guesses')
            playing = False
            replay = input('Do you want to play again? (y/n)')
            if(replay == 'y'):
                playing = True
                guesses = 0
                num = random.randrange(max)
            else :
                print('Thanks for playing')
                quit() 

        elif (guess_int < num) :
          print('Your guess was too low!')
          guesses = guesses + 1
        else :
            print('Your guess was too high!')
            guesses = guesses + 1         

guessing()        