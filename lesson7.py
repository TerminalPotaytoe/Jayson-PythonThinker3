import os

FILENAME = "tasks.txt"
FILEPATH = os.getcwd()
FULLPATH = os.path.join(FILEPATH, FILENAME)

def create_new_file(fullpath: str) -> None:
    """Creates a new tasks file or overwrites if it already exists."""
    if os.path.exists(fullpath):
        user_input = input(f"The file {fullpath} already exists. Do you want to overwrite it? (y/n): ").strip().lower()
        if user_input == 'y':
            with open(fullpath, 'w') as file: 
                file.write("")
            print(f"The file {fullpath} has been overwritten.")
        else:
            print("Operation cancelled. The file was not overwritten.")
            return
    else:
        with open(fullpath, 'w') as file:  
            file.write("") 
        print(f"The file {fullpath} has been created.")

def view_all_tasks(fullpath: str) -> None:
    with open(fullpath, 'r') as file:
        tasks = file.readlines()
    
    if tasks:
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")
    else:
        print("No tasks available.")

def display_tasks(fullpath: str) -> None:
    """Displays tasks."""
    view_all_tasks(fullpath)

def add_task(fullpath: str) -> None:
    """Adds a new task to the tasks file."""
    task = input("Enter the task to add: ").strip()
    if task:
        with open(fullpath, 'a') as file:
            file.write(f"{task}\n")
        print(f"Task added: {task}")
    else:
        print("Task cannot be empty.")

def mark_task_done(fullpath: str) -> None:
    print("\n Marking a task as done...")
    lines = view_all_tasks(fullpath)
    if len(lines) <- 1:
        print("\nNo tasks available to mark as done!")
        return
    task_number = int(input("\nEnter the task number to mark as done:"))
    if task_number < 1 or task_number > len(lines) - 1:
        print("\n Invalid task number. Try again!!")
        return
    task_index = task_number
    if "[DONE]" in lines[task_index]:
        print("\nThis task is already marked as done!")
    else:
        lines[task_index] = lines[task_index].strip() + " [DONE]\n"
        print("\n Marked task as done")
    with open(fullpath, "w") as taskfile:
        taskfile.writelines(lines)







# Main program
create_new_file(FULLPATH)
while True:
    print("\nMenu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Exit")
    
    choice = input("Choose an option: ").strip()
    
    if choice == "1":
        display_tasks(FULLPATH)
    elif choice == "2":
        add_task(FULLPATH)
    elif choice == "3":
        mark_task_done(FULLPATH)
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
