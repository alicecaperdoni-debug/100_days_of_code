# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added

import art
print(art.logo)
print("Welcome!")
name_bid = {}

new_bidder = True
while new_bidder == True:
    name = input("Enter your name:\n")
    bid = int(input("Enter your bid:\n"))
    name_bid[name] = bid
    new = input("Are there any other bidders? Type \"yes\" or \"no\".\n").lower()
    if new == "no":
        new_bidder = False
    elif new == "yes":
        print("\n" * 20)

# TODO-4: Compare bids in dictionary

max_bid = 0
winner = ""
for name in name_bid:
    if name_bid[name] > max_bid:
        max_bid = name_bid[name]
        winner = name

print(f"The winner is {winner} with {max_bid}.")
