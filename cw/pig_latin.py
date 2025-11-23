# # def pig_it(text):
# #     pig = []

# #     words = text.split(' ')
    
# #     for word in words:
# #         if word.isalpha():

# #             new_word = word[1:]

# #             first_char = word[0:1]

# #             word = new_word + first_char + 'ay'
# #             pig.append(word)

# #         else:
# #             word = word + 'ay'
# #             pig.append(word)

# #     print(" ".join(pig))

# # pig_it('O tempora o mores !')

# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

def pig_it(text):
    lst = text.split()
    return ' '.join(word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst)

# first iterate through the list, each index is called word

# IF the word were looking at is only alphabetical letters then we can change this index to the word's character minus the first char + end char + 'ay'
# otherwise just leave it and iterate through it as normal dont do anything
# once done and all changes are done join the thing into a string and return it