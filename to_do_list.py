def create_list(task_list):
    def add():
        task = input("Enter task: ")
        task_list.append(task)
        print("Added Successfully!!\n")
        return task

    while True:
        add()  # Add the task
        choice = input("\nDo you want to add task again? (yes/no): ").lower()
        if choice != "yes":
            print("\nCurrent Task List:")
            for i, task in enumerate(task_list, start=1):
                print(f"Task {i}: {task}")
            break

    return task_list

def update_list(task_list):
    print("\nCurrent Task List:")
    for i, task in enumerate(task_list, start=1):
        print(f"Task {i}: {task}")
    num = int(input("Enter The Number of The Task: "))
    if 1 <= num <= len(task_list):
        new_task = input("Enter the updated task: ")
        task_list[num - 1] = new_task
        print("Updated Successfully!!\n")
    else:
        print("Invalid task number!")

    print("\nUpdated Task List:")
    for i, task in enumerate(task_list, start=1):
        print(f"Task {i}: {task}")

    return task_list

def delete_list(task_list):
    print("\nCurrent Task List:")
    for i, task in enumerate(task_list, start=1):
        print(f"Task {i}: {task}")
    num = int(input("Enter The Number Of The Task: "))
    if 1 <= num <= len(task_list):
        task_list.pop(num - 1)
        print("Deleted Successfully!!\n")
    else:
        print("Invalid task number!")

    print("\nCurrent Task List:")
    for i, task in enumerate(task_list, start=1):
        print(f"Task {i}: {task}")

def complete_list(task_list):
    print("\nCurrent Task List:")
    for i, task in enumerate(task_list, start=1):
        print(f"Task {i}: {task}")
    num = int(input("Enter The Number of The Task Which is Completed: "))
    completed_tasks = []

    if 1 <= num <= len(task_list):
        completed_tasks.append(task_list.pop(num - 1))
        print("Congrats! You Completed This Task.\n")
    else:
        print("Invalid task number!")

    print("\nCurrent Task List:")
    for i, task in enumerate(task_list, start=1):
        print(f"Task {i}: {task}")

    if completed_tasks:
        complete = input("Do You Want To See Completed Task? (yes/no): ").lower()
        if complete == "yes":
            for i, task in enumerate(completed_tasks, start=1):
                print(f"Completed Task {i}: {task}")

# Main function
main_list = []
print("Welcome!")
while True:
    print("\n1. Create\n2. Update\n3. Delete\n4. Complete\n5. Finish/Exit")
    choice = int(input("Enter Your Choice Here: "))
    if choice == 1:
        create_list(main_list)
    elif choice == 2:
        update_list(main_list)
    elif choice == 3:
        delete_list(main_list)
    elif choice == 4:
        complete_list(main_list)
    elif choice == 5:
        print("Thanks for using our service :)")
        break
    else:
        print("Wrong Input, Try Again!")
