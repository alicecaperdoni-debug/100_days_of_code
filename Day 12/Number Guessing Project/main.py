import random
import art

COMPUTER_CHOICE = random.randrange(1, 101)
print(art.logo)
print("Welcome to the Number Guessing Game!")
print ("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type \"easy\" or \"hard\":\n").lower()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

game_continue = True

while game_continue and attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess == COMPUTER_CHOICE:
        print(f"You got it! The answer was {COMPUTER_CHOICE}")
        game_continue = False
    elif user_guess > COMPUTER_CHOICE:
        print("Too high!")
    elif user_guess < COMPUTER_CHOICE:
        print("Too low!")
    attempts -= 1
    if attempts > 0:
        print("Guess again.")

if attempts == 0:
    print("You've run out of guesses.")
