import random
import art
from game_data import data
score = 0
profile_a = random.choice(data)
profile_b = random.choice(data)

def account_format (account):
      name = account['name']
      job = account['description']
      country = account['country']
      return f"{name}, a {job}, from {country}."

def check_answer():
      answer = input("Who has more followers? Type \"A\" or \"B\".").lower()
      print("\n" * 20) # gli spazi e i vari loghi sono così per copiare come ha fatto l'insegnante, anche se non mi piace
      print(art.logo)
      if ((answer == "a" and profile_a['follower_count'] > profile_b['follower_count']) or
                (answer == "b" and profile_b['follower_count'] > profile_a['follower_count'])):
            global score
            score += 1
            return True
      else:
            return False

game_continue = True
print(art.logo)
while game_continue:
      profile_a = profile_b
      profile_b = random.choice(data)

      print(f"Compare A: {account_format(profile_a)}")
      print(art.vs)
      print(f"Against B: {account_format(profile_b)}")

      if check_answer():
            print(f"You're right! Current score: {score}")
      else:
            print(f"Sorry, that's wrong! Final score: {score}")
            game_continue = False