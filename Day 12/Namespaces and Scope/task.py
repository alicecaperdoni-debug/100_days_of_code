enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
# It prints "2" because inside the function

print(f"enemies outside function: {enemies}")
# It prints "1" because outside the function
