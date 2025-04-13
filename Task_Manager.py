import os

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")

def list_tasks():
    if not tasks:
        print("No tasks to show.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Task Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            list_tasks()
            input("Press Enter to continue...")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
