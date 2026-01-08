w1 = input("enter the first word ") # normally i would strip() and upper() this but q says all input is valid
w2 = input('enter the second word ') 


# i want to count the letters in each word

count1 = {}
count2 = {}

for ch in w1:
    count1[ch] = count1.get(ch,0) + 1 # access the next letter in the word

for ch in w2:
    count2[ch] = count2.get(ch,0) + 1

gunna_form = True # keeep track whether the word is formable 
for ch in count1:
    if count1[ch] > count2.get(ch,0):
        gunna_form = False
        break # we break because only need one instance for us to know whether the word can be formed or not.

if gunna_form:
    print(f"{w1} can be formed from {w2}") # f string literal to make it look nice
else:
    print(f"{w1} cannot be formed from {w2}")        



