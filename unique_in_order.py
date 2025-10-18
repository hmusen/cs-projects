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