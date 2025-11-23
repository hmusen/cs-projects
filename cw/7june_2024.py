def bouncy_boi():
    while True:
        number = input("Enter a number, and its bounciness will be checked ")
        try:
            number = int(number) # check if it is a integer, if not except branch will run
            break
        except ValueError: # reprompts user to enter an integer
            print("Please enter an INTEGER")
    
    num = str(number)
    for i in range(len(num) - 1): # increasing
        if num[i] > num[i+1]:
            increasing = False
            break
        else:
            increasing = True
    if increasing:
        print(f"{number} is increasing!")
    else:
        print(f"{number} is not increasing :(")

bouncy_boi()
