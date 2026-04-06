def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did non provide valid inputs"
        # to escape the function, it will print "none" if we don't write anything
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
    # after "return" it exits the function, the code below will not be executed


print(format_name(input("What is your first name?"), input("What is your last name?")))
