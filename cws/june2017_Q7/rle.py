string = input("Enter a string that will be converted to RLE: ").upper()
output = ''

count = 1

for char in range(1, len(string)):
    if string[char] == string[char-1]:
        count += 1
    else:
        output += f"{string[char-1]} {count} "

        count = 1



print(output)

# i want to check how many of a letter there are in a row

# start at a. Ok nice there is one. 
# look at the next one, yes there is another a. Thats 2
# look at the next one there is another a nice. That's 3
# look at the next one there is another one that's 4.
# look at the next one. Woah. No. Its not equal to a so stop there. A has 4.
# then we move to the index of the string[5] or in fact string[how many repetitions + 1]

#. aaaabb