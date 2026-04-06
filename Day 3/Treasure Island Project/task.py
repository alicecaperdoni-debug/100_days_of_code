print(r'''
                   ___    /\
                  `---|  /%%\/\
                     ,`./,--.\%\
                    /%%%\|  |--.\
                   /,---.|[]|  |
                    |]_'||__| [|
                    ||]|[|]|[| |
               ._..-':\._ ''/`-'.._.
        ._._.  |  _.:"'|-'`|-..__.:|  ._._.
        '._,'_.''_    _|  _| .-. ``'._'._.'
         | |_  ,'.\  '-| '-| |_|   [] _| |
    _____|]|-'|,++:_   ||] |_     _  '-|[|_________
    ~  ,-|`|  |+++|-'  |  _|-'   '-'   |.|  ~   SSt
      ~) |_|__||  |    ; '-:         __|_|`-.___ ~
    _  \-._..''`--:.__/-'   \__..--''    __...-,'__
     `-,-'    _.-'-.   `---''   _____..')..-~~'|\
       `-._.-'`-._'`)         ,'`_..-~~' ~_____;'
            `. ~~ `.`.________`.( ~~  ___)
              )    ~`.\ '  '    ,'  ~\
            ,'|  ~    ')__:__:_( ~   |)
             `-...______________....-'
''')
print("Welcome to the haunted castle.")
print("Your mission is to find the exit.")

first_door = input('You wake up in the dungeons of a castle. There are two doors'
                   ' in front of you. Type "right" or "left".').lower()

# "input \n" per avere la risposta a capo.
# if first_door == "left": solution; else: "game over" (game over for all the wrong inputs)

if first_door == "right":
    print('You find the guard. You start a fight and you die.')
elif first_door == "left":
    first_corridor = input('You find the stairs. At the end of the stairs you '
                           'find a corridor. You can go "left" or "right".').lower()

    if first_corridor == "left":
        print("There is a hole in the ground. You fall and die.")
    elif first_corridor == "right":
        follow_voice = input('You hear someone whispering. Do you follow the '
                             'voice? Type "yes" or "no".').lower()

        if follow_voice == "no":
            print("You are stuck in the castle.")
        elif follow_voice == "yes":
            print ("You follow the voice and you exit the castle!")
        else:
            print("Wrong input.")

    else:
        print("Wrong input.")
else:
    first_door = input("Wrong input.")
