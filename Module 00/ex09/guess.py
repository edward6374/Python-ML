import sys
import random

def main():
    attempts = 0
    control = True
    number = random.randint(1, 99)
    while control:
        print("What's your guess between 1 and 99?\n>> ", end="")
        guess = input()
        if guess == "exit":
            print("Goodbye!")
            control = False
        elif not guess.isdigit():
            print("That's not a number")
        elif int(guess) > number:
            print("Too high!")
        elif int(guess) < number:
            print("Too low!")
        elif int(guess) == number and attempts == 0:
            print("Congratulations! You've got it on your first try!")
            control = False
        elif int(guess) == number and number == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
            print("Congratulations, you've got it!\nYou won in", attempts, "attempts")
            control = False
        elif int(guess) == number:
            print("Congratulations, you've got it!\nYou won in", attempts, "attempts")
            control = False
        attempts += 1





if __name__ == "__main__":
    print('''
    \rThis is an interactive guessing game!
    \rYou have to enter a number between 1 and 99 to find out the secret number.
    \rType 'exit' to end the game.
    \rGood luck!
    ''')
    main()
