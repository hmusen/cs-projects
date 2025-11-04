is_prime = True

choice = "Y"
while choice == "Y":
    n = int(input("What number do you want to check? "))
    if n > 1:
        for divisor in range(2,n):
            if (n % divisor) == 0:
                is_prime = False
                break
        
        if is_prime == False:
            print("Is not prime")
        else:
            print("Is prime")
    
    else:
        print("Not greater than 1")

    response = input("Do you want to enter a new number? Enter Y / N? ")
    
    if response == "Y":
        choice = "Y"
    elif response == "N":
        print("No more numbers to enter 😢. We're done here.")
        break

