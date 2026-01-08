def integer_strings(n):
    text = ''
    for i in range(1,102):
         text += str(i)
        
    count = 0
    for digit in text:
         if digit == '5':
              count = count + 1
    return text, count
   
print(integer_strings(1))

# answer is 20

