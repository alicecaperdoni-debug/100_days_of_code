import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_score = 0
computer_score = 0

def deal_card():
    random_card = random.choice(cards)
    return random_card

def calculate_score(card_list):
    if sum(card_list) == 21:
        return 0
    elif sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        return sum(card_list)
    else:
        return sum(card_list)

def compare():
    if user_score == computer_score:
        print(f"It's a draw!\nYour final hand: {user_cards}, your final score: {user_score}.\nComputer final hand:"
              f"{computer_cards}, computer final score: {computer_score}.")
    elif computer_score == 0:
        print(f"You lose!\nYour final hand: {user_cards}, your final score: {user_score}.\nComputer final hand:"
              f"{computer_cards}, computer final score: {computer_score}.")
    elif user_score == 0:
        print(f"You win!\nYour final hand: {user_cards}, your final score: {user_score}.\nComputer final hand:"
              f"{computer_cards}, computer final score: {computer_score}.")
    elif user_score > 21:
        print(f"You lose!\nYour final hand: {user_cards}, your final score: {user_score}.\nComputer final hand:"
              f"{computer_cards}, computer final score: {computer_score}.")
    elif computer_score > 21:
        print(f"You win!\nYour final hand: {user_cards}, your final score: {user_score}.\nComputer final hand:"
              f"{computer_cards}, computer final score: {computer_score}.")
    else:
        if user_score > computer_score:
            print(f"You win!\nYour final hand: {user_cards}, your final score: {user_score}.\nComputer final hand:"
                  f"{computer_cards}, computer final score: {computer_score}.")
        else:
            print(f"You lose!\nYour final hand: {user_cards}, your final score: {user_score}.\nComputer final hand:"
                  f"{computer_cards}, computer final score: {computer_score}.")

play_again = True
while play_again:
    user_cards.clear()
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.clear()
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    new_card = True
    game_end = False

    while new_card and not game_end:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}.\n Computer's first card: {computer_cards[0]}.")
        if user_score == 0:
            new_card = False
            game_end = True
            print(f"You win!\nYour final hand: {user_cards}, your final score: {user_score}.\nComputer final hand:"
                  f"{computer_cards}, computer final score: {computer_score}.")
        elif computer_score == 0 or user_score > 21:
            new_card = False
            game_end = True
            print(f"You lose!\nYour final hand: {user_cards}, your final score: {user_score}.\nComputer final hand:"
                  f"{computer_cards}, computer final score: {computer_score}.")
        else:
            draw_again = input("Do you want to draw another card? \"y\" or \"n\":")
            if draw_again == "y":
                user_cards.append(deal_card())
            elif draw_again == "n":
                new_card = False

    comp_score_ok = True
    while comp_score_ok and not game_end:
        if computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            if computer_score > 21:
                comp_score_ok = False
                print(f"You win!\nYour final hand: {user_cards}, your final score: {user_score}.\nComputer final hand:"
                  f"{computer_cards}, computer final score: {computer_score}.")
        else:
            comp_score_ok = False

    if not game_end:
        compare()

    choice = input("Do you want to play again? Type \"y\" or \"n\".")

    if choice == "n":
        play_again = False

