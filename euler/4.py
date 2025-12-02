# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# smallest = 0
# loop through and do 0 % i. If in one instance 0 % i != 0 increment 0 by 1 and repeat for this new number.

def smallest():
    number = 1
    satisfied = False

    while satisfied == False:
        is_divisible = True
        for i in range(1, 21):
            if number % i != 0:
                is_divisible = False
                break
        
        if is_divisible:
            satisfied = True
        else:
            number += 1
    
    print(number) 



smallest()

# why is this so slow