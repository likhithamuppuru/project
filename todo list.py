import datetime

def print_tasks(task_list):
    priority_rank = {"high": 1, "medium": 2, "low": 3}
    task_list.sort(key=lambda x: (priority_rank.get(x[1], 3), x[2]))
    for i, row in enumerate(task_list, 1):
        print(f"{i}: {row[0]}, Priority: {row[1]}, Added on: {row[2]}")

def add_task(task_list):
    task = input("Enter a task: ")
    priority = input("Enter the priority (high, medium, low): ").lower()
    if priority not in ["high", "medium", "low"]:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        return
    task_list.append([task, priority, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

def delete_task(task_list):
    if not task_list:
        print("No tasks to delete.")
        return
    try:
        task_number = int(input("Enter the task number to delete: "))
        del task_list[task_number - 1]
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

def edit_task(task_list):
    if not task_list:
        print("No tasks to edit.")
        return
    try:
        task_number = int(input("Enter the task number to edit: "))
        new_task = input("Enter the new task: ")
        task_list[task_number - 1][0] = new_task
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

task_list = []

while True:
    print("""TODO List Management System
    1: Add
    2: Delete
    3: Edit
    4: Print
    5: Quit""")
    choice = input("Choose an option: ")
    if choice == "1":
        add_task(task_list)
    elif choice == "2":
        delete_task(task_list)
    elif choice == "3":
        edit_task(task_list)
    elif choice == "4":
        print_tasks(task_list)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please choose a valid option.")


