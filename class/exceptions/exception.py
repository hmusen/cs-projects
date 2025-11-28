usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']


def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    try:
        number = int(usernumber)
    except ValueError:
        print("You must type in a number.")
        return
    try:
        print("Welcome", usernames[number], "user number", number,".")
    except IndexError:
         print('List index is out of range')
         return
    try: 
        division = 301 / number
    except ZeroDivisionError:
        print("You can't divide by zero!")
        return
    print(f"301 divided by {number} = {division}")

while True:
    # try:
        inp = input("\nType in a number: ")
        login_unhandled(inp)
    # except IndexError:
    #     print("That user number does not exist.")


    