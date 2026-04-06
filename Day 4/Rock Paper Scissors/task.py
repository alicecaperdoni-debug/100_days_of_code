rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
player_choice = int(input('What do you choose? Type "0" for rock, "1" for '
                               'paper, and "2" for scissors.\n'))
#game_images = [rock, paper, scissors]
# print(game_images[user_choice])
if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
else:
    print('Invalid choice, start again.')

computer_choice = random.randint(0,2)
# print("Computer chose:"
# print(game_images[computer_choice])

if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if player_choice == computer_choice:
    print('Its a draw')
elif (((player_choice == 0 and computer_choice == 2) or
     (player_choice == 1 and computer_choice == 0)) or
     (player_choice == 2 and computer_choice == 1)):
    print('You win')
else:
    print('You lose')

#game_images = [rock, paper, scissors]
# if player_choice >= 0 and player_choice <=2:
# print(game_images[user_choice])
# computer_choice = random.randint(a:0, b:2)
# print("Computer chose:"
# print(game_images[computer_choice])

# if player_choice >= 3 or player_choice < 0:
    # print("You typed an invalid number. You lose!")
# elif player_choice == 0 and computer_choice == 2:
    # print("You win!)
# elif computer_choice == 0 and player_choice == 2:
    # print("You lose!")
# elif computer_choice > player_choice:
    # print("You lose!")
# elif player_choice > computer_choice:
    # print("You win!")
# elif computer_choice == player_choice:
    # print("It's a draw!")
