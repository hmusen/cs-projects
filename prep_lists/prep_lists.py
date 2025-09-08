name_list = ['Alp', 'Carter', 'Longyu', 'Samuel', 'Teo', 'Ryan', 'Oscar', 'George', 'Isaac', 'Kevin', 'Henry', 'Henry', 'Papa', 'Aidan', 'Thomas']

for i in range(3):
    name = input("Type in a name: ")
    name_list.append(name)

print(name_list)

print("The third name is ", name_list[2])

print("The last seven names are ", name_list[-7:])

# initialize variables
total = 0
largest = None
smallest = None

for i in range(5):
    number = int(input("Enter a number: "))
    total += number

    if largest is None or number > largest:
        largest = number
    if smallest is None or number < smallest:
        smallest = number

mean = total / 5

print("Total is", total)
print("Mean is", mean)
print("Largest is", largest)
print("Smallest is", smallest)
