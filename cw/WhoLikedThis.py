names = ["Peter", "James", "Adam", "David"]

def likes():
    global length
    length = len(names)
    if not names:
        print( "no one likes this")
    elif length == 1:
        print(f"{names[0]} likes this")
    elif length == 2:
        print(f"{names[0]} and {names[1]} like this")
    elif length == 3:
        print(f"{names[0]}, {names[1]} and {names[2]} like this")
    else:
        print(f"{names[0]}, {names[1]} and {length-2} others like this")
         
likes()

# if the length is greater than two, say that the first two people like it and len-2 others do as well.