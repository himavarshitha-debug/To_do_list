```python
# ==========================================
# TESTBENCH FOR TO-DO LIST MANAGEMENT SYSTEM
# ==========================================

# Import the main program
import todo_list


# ------------------------------------------
# TEST 1: ADD TASK
# ------------------------------------------

todo_list.tasks.clear()

test_task = {
    "name": "Python Assignment",
    "description": "Complete Python assignment",
    "category": "College",
    "priority": "High",
    "due_date": "15-08-2026",
    "reminder": "14-08-2026 06:00 PM",
    "status": "Pending"
}

todo_list.tasks.append(test_task)

if len(todo_list.tasks) == 1:
    print("TEST 1 - Add Task: PASS")
else:
    print("TEST 1 - Add Task: FAIL")


# ------------------------------------------
# TEST 2: CHECK TASK DETAILS
# ------------------------------------------

task = todo_list.tasks[0]

if (task["name"] == "Python Assignment" and
    task["category"] == "College" and
    task["priority"] == "High" and
    task["status"] == "Pending"):

    print("TEST 2 - Task Details: PASS")
else:
    print("TEST 2 - Task Details: FAIL")


# ------------------------------------------
# TEST 3: MARK TASK AS COMPLETED
# ------------------------------------------

todo_list.tasks[0]["status"] = "Completed"

if todo_list.tasks[0]["status"] == "Completed":
    print("TEST 3 - Complete Task: PASS")
else:
    print("TEST 3 - Complete Task: FAIL")


# ------------------------------------------
# TEST 4: CHECK COMPLETED TASK
# ------------------------------------------

completed_count = 0

for task in todo_list.tasks:
    if task["status"] == "Completed":
        completed_count += 1

if completed_count == 1:
    print("TEST 4 - Completed Task Check: PASS")
else:
    print("TEST 4 - Completed Task Check: FAIL")


# ------------------------------------------
# TEST 5: ADD PROJECT TASK
# ------------------------------------------

project_task = {
    "name": "Smart Waste Management",
    "description": "Complete project documentation",
    "category": "Project",
    "priority": "High",
    "due_date": "20-08-2026",
    "reminder": "19-08-2026 05:00 PM",
    "status": "Pending"
}

todo_list.tasks.append(project_task)

if len(todo_list.tasks) == 2:
    print("TEST 5 - Add Project Task: PASS")
else:
    print("TEST 5 - Add Project Task: FAIL")


# ------------------------------------------
# TEST 6: SEARCH TASK
# ------------------------------------------

search_keyword = "waste"
found = False

for task in todo_list.tasks:
    if search_keyword.lower() in task["name"].lower():
        found = True
        break

if found:
    print("TEST 6 - Search Task: PASS")
else:
    print("TEST 6 - Search Task: FAIL")


# ------------------------------------------
# TEST 7: CATEGORY CHECK
# ------------------------------------------

category = "Project"
category_found = False

for task in todo_list.tasks:
    if task["category"].lower() == category.lower():
        category_found = True
        break

if category_found:
    print("TEST 7 - Task Category: PASS")
else:
    print("TEST 7 - Task Category: FAIL")


# ------------------------------------------
# TEST 8: REMINDER CHECK
# ------------------------------------------

if todo_list.tasks[1]["reminder"] == "19-08-2026 05:00 PM":
    print("TEST 8 - Reminder: PASS")
else:
    print("TEST 8 - Reminder: FAIL")


# ------------------------------------------
# TEST 9: DELETE TASK
# ------------------------------------------

initial_count = len(todo_list.tasks)

todo_list.tasks.pop(1)

if len(todo_list.tasks) == initial_count - 1:
    print("TEST 9 - Delete Task: PASS")
else:
    print("TEST 9 - Delete Task: FAIL")


# ------------------------------------------
# FINAL RESULT
# ------------------------------------------

print("------------------------------------------")
print("TO-DO LIST TESTBENCH COMPLETED")
print("------------------------------------------")
```
