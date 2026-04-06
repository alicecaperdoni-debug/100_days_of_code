capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested list in Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

# print Lille
# print(travel_log["France"][1])

# print from a nested list
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Nested dictionary in a dictionary
travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon",],
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "num_times_visited": 5,
    }
}

# print Stuttgart
print(travel_log["Germany"]["cities_visited"][2])
