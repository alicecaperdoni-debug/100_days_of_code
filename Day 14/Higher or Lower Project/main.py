import random
from game_data import data

profile_a = random.choice(data)
profile_b = random.choice(data)

print(f"Compare A: {profile_a['name']}, {profile_a['description']}, from "
      f"{profile_a['country']}")
print(f"Compare B: {profile_b['name']}, {profile_b['description']}, from "
      f"{profile_b['country']}")

answer = input("Who has more followers? Type \"A\" or \"B\".").lower()


