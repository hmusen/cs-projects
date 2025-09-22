# Step 1: Make a function that allows a user to make a note and add lines to it.
import os 
import subprocess  
import stat


def create():

    filename = input("Name your file: ") + ".txt"

    # loop here, adding a new input until stop 

    state = True
    i = 1
    
    print("Say 'STOP' to exit")
    while state: # while state is true
        
        line = input(f"New line ({i}): ")
        if line.strip().upper() == "STOP":
            state = False
        else:
            with open(filename, 'a') as file:
                file.write(line + "\n")
            i = i + 1

    menu()   

def view():
    # toView = input("Enter the filename of the file you would like to view. Don't include the branch.") + ".txt"

    chosen = False
    while not chosen:
        fileName = input("Enter the textfile you'd like to open (without extension): ") + ".txt"
        if os.path.exists(fileName):
            try:
                subprocess.run(['open', fileName])
                print("Opened succesfully")
                chosen = True
            except Exception as e:
                print("error was", e) # error not related to entering of filename
        else:
            print("File does not exist. Try again.")

    menu()

def edit():
    fileName = input("Enter the textfile you'd like to edit (without extension) ") + '.txt'

   
    with open(fileName, 'r') as file:
            lines = file.readlines()
    
    if not lines:
        print('the file is empty')
    
    print("------File content------")
    for i, line in enumerate(lines):
         print(f"{i}:", line.strip())
    print("------------------------")

    line_number = int(input("Which line would you like to edit? "))

    done = False
    while not done:
        if 0 <= line_number <= len(lines):
            newText = input("Enter the new text for that line: ")
            
            # Replace the line
            lines[line_number] = newText + "\n"
            
            print(f"Line number {line_number} is now: {newText}")
            done = True  # exit the loop

            print("------File content------")
            for i, line in enumerate(lines):
                print(f"{i}:", line.strip())
            print("------------------------")
        else:
            print("Invalid line number. Please enter a valid line number.")
            line_number = int(input("Which line would you like to edit? "))


    menu()

def menu():

    done = False
    while done != True:
        try:
            choice = int(input("1. Create a file \n2. View and Display a file \n 3. Edit a file \n\n"))
            if choice == 1:
                    create()
                    done = True
            elif choice == 2:
                    view()
                    done = True

            elif choice == 3:
                    edit()
                    done = True

            elif choice < 1 or choice > 3:
                    print("Choose a valid choice")
                    done = False
        except ValueError:
            print("ENTER A NUMBER! ❌")

menu()