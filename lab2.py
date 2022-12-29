
import random

def main():
    counter=1
    number=random.randint(1,100)
    guess= int(input('What number between 1 and 100 would you like to guess?:'))
    while guess < 1 or guess >100:
            guess=int(print('Your number is not between 1 and 100. Please re-guess:'))
    while guess != number: 
        
            
        if guess<number:
            print('Your guess is too low!')
        else:
            print('Your guess is too high!')

        guess=int(input('Guess again!:'))
        while guess < 1 or guess >100:
            guess=int(print('Your number is not between 1 and 100. Please re-guess:'))
        counter+=1
    print('Congratulations! You guessed the number!')
    print('It took you',counter, 'tries!')
   
main()
