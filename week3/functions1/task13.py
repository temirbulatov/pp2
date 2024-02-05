#guess the num
import random
import math

def guess_the_number(player_name):
    targetnum = random.randint(1, 20)
    attempts = 0

    print(f"Hello, {player_name}! I am thinking of a number between 1 and 20.")
    print("Take a guess.")

    while True:
        userguess = int(input())
        attempts += 1

        if userguess < targetnum:
            print("Your guess is too low.")
            print("Take a guess.")
        elif userguess > targetnum:
            print("Your guess is too high.")
            print("Take a guess.")
        else:
            print(f"Good job, {player_name}! You guessed my number in {attempts} guesses!")
            break



player_name = input("Hello! What is your name? ")
guess_the_number(player_name)
