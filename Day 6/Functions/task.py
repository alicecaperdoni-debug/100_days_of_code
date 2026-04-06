# def my_function():
#     print("Hello")
#     print("Bye")
#
# my_function()

# Reeborgs
#     def turn_right():
#         turn_left()
#         turn_left()
#         turn_left()
#
#     def jump():
#         move()
#         turn_left()
#         move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#         turn_left()
#
      # jump 6 times (0 - 5)
#     for step in range(6):
#         jump()

## versione While
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1

# different jumps project
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     turn_right()
#     move()
#     turn_right()
#     move()
#
#
# while not at_goal():
#     while is_facing_north() == True:
#         if wall_on_right():
#             move()
#         else:
#             jump()
#     if wall_in_front():
#         turn_left()
#     else:
#         move()

# Solution
# def jump():
#    turn_left()
#    while wall_on_right():
#       move()
#    turn_right()
#    move()
#    turn_right()
#    while front_is_clear():
#        move()
#
# while not_at_goal():
#    if wall_in_front():
#        jump()
#    else:
#    move()

## Maze
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()