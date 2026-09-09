
tasks = []

def show_menu():
    print("\n1. Add task\n2. View tasks\n3. Remove task\n4. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def remove_task():
    view_tasks()
    try:
        num = int(input("Enter task number to remove: "))
        tasks.pop(num - 1)
        print("Task removed!")
    except (ValueError, IndexError):
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        break
    else:
        print("Invalid option.")