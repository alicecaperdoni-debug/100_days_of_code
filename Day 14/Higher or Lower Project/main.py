import random
import art
from game_data import data
score = 0

profile_a = random.choice(data)
profile_b = random.choice(data)
print(art.logo)

game_continue = True
while game_continue:
      print(f"Compare A: {profile_a['name']}, {profile_a['description']}, from "
            f"{profile_a['country']}")
      print(art.vs)
      print(f"Compare B: {profile_b['name']}, {profile_b['description']}, from "
            f"{profile_b['country']}")

      answer = input("Who has more followers? Type \"A\" or \"B\".").lower()

      if ((answer == "a" and profile_a['follower_count'] > profile_b['follower_count']) or
              (answer == "b" and profile_b['follower_count'] > profile_a['follower_count'])):
            score += 1
            print(art.logo)
            print(f"You're right! Current score: {score}")
      else:
            print(f"You're wrong! Final score: {score}")
            game_continue = False

      profile_a = profile_b
      profile_b = random.choice(data)
