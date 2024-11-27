#Final Project for CNE 330
#A python to-do list
tasks = []
#main loop
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Remove Tasks")
        print("4. Mark/Unmark Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_tasks()
        elif choice == "3":
            remove_tasks()
        elif choice == "4":
            toggle_task()
        elif choice == "5":
            print("Thank You!")
            break
        else:
            print("Invalid Option!")

#Display's tasks and their status
def display_tasks():
    if not tasks:
        print("There are no tasks!")
    else:
        print("Your To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "[Done]" if task['done'] else "[Not Done]"
        print(f"{i}. {status} {task['description']}")

#Add's a new task
def add_tasks():
    task_desc = input("Enter Description: ")
    if task_desc:
        tasks.append({"description": task_desc, "done": False})
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")

#Removes Tasks
def remove_tasks():
    display_tasks()
    try:
        task_num = int(input("Enter Task Number: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print("Task removed successfully!")
        else:
            print("Invalid Task Number!")
    except ValueError:
        print("Invalid Task Number!")

#Checks to indicate if tasks have been completed
def toggle_task():
    display_tasks()
    try:
        task_num = int(input("Enter Task Number: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = not tasks[task_num - 1]["done"]
            status = "[Done]" if task_num <= len(tasks) else "[Not Done]"
            print(f"{status} {tasks[task_num - 1]['description']}")
        else:
            print("Invalid Task Number!")
    except ValueError:
        print("Invalid Task Number!")

if __name__ == "__main__":
    main()