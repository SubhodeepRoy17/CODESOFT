import sys

def display_menu():
    print("To-Do List Application")
    print("=======================")
    print("1. View List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print()

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list so far...")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.\n")

def update_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to update: "))
    if 1 <= task_num <= len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_num - 1] = new_task
        print("Task updated successfully.\n")
    else:
        print("Invalid task number.\n")

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(tasks):
        tasks.pop(task_num - 1)
        print("Task deleted successfully.\n")
    else:
        print("Invalid task number.\n")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
