# Codewars: Unique In Order 6 Kyu Solution

def unique_in_order(sequence):
    new_list = list(sequence) # takes a string and separates each char into its own element in a list

    result = []
    for i in range (len(new_list)-1):
        if new_list[i] != new_list[i+1]:
            result.append(new_list[i])
    if new_list:
        result.append(new_list[-1])
    print(result)

unique_in_order("ABAAAABBA")

# I may get type errors if I try to access the next element of something that doesn't exist, so go the length and subtract one. 

# In this one, instead of removing from the list itself which will mess up the loop (nono), put the non-duplicated items into a new array just leave out 

# this solution is a bit different. It looks through each element and says is it equal to the next one, if it is, it just skips it instead of appending it, the next iteration will either do the same thing again or have a different i+1, so it will append i. Allowing you to remove all duplicates
    
# If you want to turn a string or any data type into a list, use list(variable_to_convert)

# Use my_list[-1] to access the last element of an array. E.g x = [1,23,45,63,"Meow"]. Doing print(x[-1]) will give you the last element, in other words, "meow"