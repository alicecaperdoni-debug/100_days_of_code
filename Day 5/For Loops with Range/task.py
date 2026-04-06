# Range function with for Loop

# Remember a >= x < b; c = step size
# for number in range(1,11, 3):
#     print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

for i in range(1, 101):
    j = i % 3
    k = i % 5
    if  j == 0 and k == 0:
        print("Fizzbuzz")
    elif j == 0:
        print("Fizz")
    elif k == 0:
        print("Buzz")
    else:
        print(i)


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)