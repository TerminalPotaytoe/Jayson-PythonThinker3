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

def view_tasks(fullpath: str) -> None:
    """Displays the tasks from the file."""
    if not os.path.exists(fullpath):
        print("No tasks found. The file does not exist.")
        return
    
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
    view_tasks(fullpath)

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
    """Marks a task as done by removing it or appending 'done' to it."""
    if not os.path.exists(fullpath):
        print("No tasks found. The file does not exist.")
        return

    with open(fullpath, 'r') as file:
        tasks = file.readlines()

    if not tasks:
        print("No tasks to mark as done.")
        return

    view_tasks(fullpath)  # Display the current tasks
    try:
        task_number = int(input("Enter the number of the task to mark as done: "))
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1].strip()
            # Marking the task as done by appending " [done]"
            tasks[task_number - 1] = f"{task} [done]\n"
            
            with open(fullpath, 'w') as file:
                file.writelines(tasks)
            
            print(f"Task marked as done: {task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

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
