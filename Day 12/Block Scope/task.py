game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = "" # the variable has to be created, always available to be accessed
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)
