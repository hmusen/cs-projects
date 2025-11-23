numeric = [0,0,0,0,0,0,0,0,0,0]

numbers = int(input("How many numbers do you want to enter?: "))

nice_list = []
for i in range(numbers):
    inputted = int(input(f'Enter number {i+1}: '))
    nice_list.append(inputted)

for i in nice_list:
    numeric[i] = numeric[i] + 1


# Find how many times the most common number appeared
largest = max(numeric)

print("The most common number appeared", largest, "times.")
