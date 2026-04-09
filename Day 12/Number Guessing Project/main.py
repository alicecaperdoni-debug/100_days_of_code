import random
COMPUTER_CHOICE = random.randrange(1, 101)

def make_guess():
    user_guess = int(input("Make a guess: "))
    if user_guess == COMPUTER_CHOICE:
        print(f"You got it! The answer was {COMPUTER_CHOICE}")
    elif user_guess > COMPUTER_CHOICE:
        print("Too high!\nGuess again.")
    elif user_guess < COMPUTER_CHOICE:
        print("Too low!\nGuess again.")


print("Welcome to the Number Guessing Game!")
print ("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type \"easy\" or \"hard\":\n").lower()

make_guess()
# if difficulty == "easy":
#     for n in range(6):

