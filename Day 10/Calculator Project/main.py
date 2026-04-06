import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo)
    should_accumulate = True
    first_number = float(input("What's the first number?"))

    while should_accumulate:
        operator = input("+\n-\n*\n/\nPick an operation:")
        second_number = float(input("What's the second number?"))
        result = operations[operator](first_number, second_number)
        print(result)

        choice = input(f"Type \"y\" to continue operating with {result}, or type \"n\" to start"
              f"a new calculation:")
        if choice == "y":
            first_number = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()


