task_list = [] # define a task list 


def addTask():
    task = input("Enter a task that you would like to do \n")
    task_list.append(task) # add the task to the task list 
    print(task_list)


def displayAllTasks(task_list):
    while True:
        response = input("Would you like to display all the tasks? (Y/N): ").strip().upper()
        if response == "Y":
            print(task_list)
            break
        elif response == "N":
            print("Okay, not displaying tasks.")
            break
        else:
            print("Please try again. Answer with 'Y' or 'N'.")

def checkTask():
    while True:
        try:
            pos = int(input("What task would you like to check? (Type its position i.e. A number) "))
            
            # Check if position is within valid range
            if 1 <= pos <= len(task_list):
                print("Task is " + task_list[pos - 1])
                break
            else:
                print("This task's position does not exist!")
        
        except ValueError:
            print("Please enter a valid number.")

def completeNextTask():
    while True:
        try:
            for i, task in range(task_list):
                print(f"{i}: {task}")

            completedIndex = int(input("\nWhich task have you completed? Enter the index: "))

            if 0 <= completedIndex < len(task_list):
                removed_task = task_list.pop(completedIndex)
                print(f"Removed: {removed_task}")
                print("Remaining tasks:", task_list)
                break
            else:
                print("Invalid index. Try again.")

        except ValueError:
            print('Please enter a valid number.')


    

def menu():
    while True:
        choice = input("What would you like to do? \n 1. Create a task \n 2. Display all tasks \n 3. Check task \n 4. Complete a task \n 5. Exit \n")
        if choice == "1":
            addTask()
        elif choice == "2":
            displayAllTasks(task_list)
        elif choice == "3": 
            checkTask()
        elif choice == "4":
            completeNextTask()
        elif choice == "5":
            break
        else:
            print("Enter a valid numbered choice")

menu()

