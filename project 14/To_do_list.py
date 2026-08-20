# ==========================================
#        TO-DO LIST MANAGEMENT SYSTEM
# ==========================================

tasks = []


# ------------------------------------------
# 1. ADD TASK
# ------------------------------------------
def add_task():
    print("\n----- ADD NEW TASK -----")

    name = input("Enter task name: ")
    description = input("Enter task description: ")
    category = input("Enter category (College/Personal/Project/Exam/Other): ")
    priority = input("Enter priority (High/Medium/Low): ")
    due_date = input("Enter due date (DD-MM-YYYY): ")
    reminder = input("Enter reminder time/date: ")

    task = {
        "name": name,
        "description": description,
        "category": category,
        "priority": priority,
        "due_date": due_date,
        "reminder": reminder,
        "status": "Pending"
    }

    tasks.append(task)

    print("\nTask added successfully!")


# ------------------------------------------
# 2. VIEW ALL TASKS
# ------------------------------------------
def view_tasks():
    print("\n----- ALL TASKS -----")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    for i in range(len(tasks)):
        print("\nTask Number:", i + 1)
        print("Task Name   :", tasks[i]["name"])
        print("Description :", tasks[i]["description"])
        print("Category    :", tasks[i]["category"])
        print("Priority    :", tasks[i]["priority"])
        print("Due Date    :", tasks[i]["due_date"])
        print("Reminder    :", tasks[i]["reminder"])
        print("Status      :", tasks[i]["status"])
        print("-----------------------------")


# ------------------------------------------
# 3. MARK TASK AS COMPLETED
# ------------------------------------------
def complete_task():
    print("\n----- COMPLETE TASK -----")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        number = int(input("Enter task number to complete: "))

        if number >= 1 and number <= len(tasks):
            tasks[number - 1]["status"] = "Completed"
            print("Task marked as completed successfully.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# ------------------------------------------
# 4. DELETE TASK
# ------------------------------------------
def delete_task():
    print("\n----- DELETE TASK -----")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        number = int(input("Enter task number to delete: "))

        if number >= 1 and number <= len(tasks):
            deleted_task = tasks.pop(number - 1)
            print("Task deleted:", deleted_task["name"])
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# ------------------------------------------
# 5. SEARCH TASK
# ------------------------------------------
def search_task():
    print("\n----- SEARCH TASK -----")

    keyword = input("Enter task name or keyword: ").lower()

    found = False

    for i in range(len(tasks)):
        if keyword in tasks[i]["name"].lower():
            print("\nTask Number:", i + 1)
            print("Task Name :", tasks[i]["name"])
            print("Category  :", tasks[i]["category"])
            print("Priority  :", tasks[i]["priority"])
            print("Due Date  :", tasks[i]["due_date"])
            print("Status    :", tasks[i]["status"])
            found = True

    if not found:
        print("Task not found.")


# ------------------------------------------
# 6. VIEW PENDING TASKS
# ------------------------------------------
def pending_tasks():
    print("\n----- PENDING TASKS -----")

    found = False

    for i in range(len(tasks)):
        if tasks[i]["status"] == "Pending":
            print("\nTask Number:", i + 1)
            print("Task Name :", tasks[i]["name"])
            print("Category  :", tasks[i]["category"])
            print("Priority  :", tasks[i]["priority"])
            print("Due Date  :", tasks[i]["due_date"])
            print("Reminder  :", tasks[i]["reminder"])
            found = True

    if not found:
        print("No pending tasks.")


# ------------------------------------------
# 7. VIEW COMPLETED TASKS
# ------------------------------------------
def completed_tasks():
    print("\n----- COMPLETED TASKS -----")

    found = False

    for i in range(len(tasks)):
        if tasks[i]["status"] == "Completed":
            print("\nTask Number:", i + 1)
            print("Task Name :", tasks[i]["name"])
            print("Category  :", tasks[i]["category"])
            print("Priority  :", tasks[i]["priority"])
            print("Due Date  :", tasks[i]["due_date"])
            print("Status    :", tasks[i]["status"])
            found = True

    if not found:
        print("No completed tasks.")


# ------------------------------------------
# 8. VIEW TASKS BY CATEGORY
# ------------------------------------------
def category_tasks():
    print("\n----- TASKS BY CATEGORY -----")

    category = input(
        "Enter category (College/Personal/Project/Exam/Other): "
    ).lower()

    found = False

    for i in range(len(tasks)):
        if tasks[i]["category"].lower() == category:
            print("\nTask Number:", i + 1)
            print("Task Name :", tasks[i]["name"])
            print("Priority  :", tasks[i]["priority"])
            print("Due Date  :", tasks[i]["due_date"])
            print("Status    :", tasks[i]["status"])
            found = True

    if not found:
        print("No tasks found in this category.")


# ------------------------------------------
# 9. VIEW REMINDERS
# ------------------------------------------
def view_reminders():
    print("\n----- TASK REMINDERS -----")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    found = False

    for i in range(len(tasks)):
        if tasks[i]["status"] == "Pending":
            print("\nTask:", tasks[i]["name"])
            print("Due Date:", tasks[i]["due_date"])
            print("Reminder:", tasks[i]["reminder"])
            found = True

    if not found:
        print("No pending reminders.")


# ------------------------------------------
# MAIN MENU
# ------------------------------------------
def main():
    while True:

        print("\n==========================================")
        print("        TO-DO LIST MANAGEMENT SYSTEM")
        print("==========================================")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. View Pending Tasks")
        print("7. View Completed Tasks")
        print("8. View Tasks by Category")
        print("9. View Reminders")
        print("10. Exit")
        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            search_task()

        elif choice == "6":
            pending_tasks()

        elif choice == "7":
            completed_tasks()

        elif choice == "8":
            category_tasks()

        elif choice == "9":
            view_reminders()

        elif choice == "10":
            print("\nThank you for using To-Do List Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main()