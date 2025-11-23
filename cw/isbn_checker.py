ISBN = []

for Count in range(13): 
    R = int(input("Please enter next digit of ISBN: "))
    ISBN.append(R)

CalculatedDigit = 0

Count = 0
while Count < 12:
    CalculatedDigit = CalculatedDigit + ISBN[Count]
    Count = Count + 1
    CalculatedDigit = CalculatedDigit + ISBN[Count] * 3
    Count = Count + 1

while CalculatedDigit >= 10:
    CalculatedDigit = CalculatedDigit - 10

CalculatedDigit = 10 - CalculatedDigit

if CalculatedDigit == 10:
    CalculatedDigit = 0

if CalculatedDigit == ISBN[12]:
    print("valid ISBN")
else:
    print('invalid ISBN')