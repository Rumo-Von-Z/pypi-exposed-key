#make a guessing game
import random

def main():
    
    random_number = random.randint(1, 10)

    guess_count = 0
    guess_limit = 3
    guess = 0
    
    
    while guess != random_number and guess_count < guess_limit:
        guess = int(input("Guess a number between 1 and 10: "))
        guess_count += 1
    
    if guess == random_number:
        print("You guessed it!")
    else:
        print("You lose!")

