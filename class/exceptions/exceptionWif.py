usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']


def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")

    number = int(usernumber)

    if number.isnumeric() == False:
        raise ValueError("You must type in a number.")
    
    print("Welcome", usernames[number], "user number", number,".")

    division = 301 / number

    if division == 0:
        raise ZeroDivisionError("can't divide by zero because number is zero.")
    
    print(f"301 divided by {number} = {division}")

while True:
    inp = input("\nType in a number: ")
    
    login_unhandled(inp)