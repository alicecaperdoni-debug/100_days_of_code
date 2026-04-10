import random

def make_guess(): # due funzioni, una make_guess ed una check_guess?
    user_guess = int(input("Make a guess: ")) # questo probabilmente va fuori; poi "Guess again:"
    if user_guess == COMPUTER_CHOICE:
        print(f"You got it! The answer was {COMPUTER_CHOICE}")
    elif user_guess > COMPUTER_CHOICE:
        print("Too high!\nGuess again.")
    elif user_guess < COMPUTER_CHOICE:
        print("Too low!\nGuess again.")

COMPUTER_CHOICE = random.randrange(1, 101)
print("Welcome to the Number Guessing Game!")
print ("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type \"easy\" or \"hard\":\n").lower()

if difficulty == "easy":
    attempts = 10
    for i in range(11): # fermare il loop se la risposta è stata trovata
        print(f"You have {attempts} attempts remaining to guess the number.")
        make_guess()
        attempts -= 1
