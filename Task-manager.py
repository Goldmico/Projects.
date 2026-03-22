print("Tasks")


print("Options:")
print("Add Task")
print("Mark tasks as completed")
print("View Tasks")
print("Delete Tasks")
print("Exit")

print("")

new_task = "No Task"
new_task_2 = "No Task"

options = input("Please enter your option: ")

while True:
    options = input("Please enter your option: ")

    if options == "Add Task":

        new_task = input("Please enter your new task name: ")
        if new_task != "":
            new_task = ("Task 1:", new_task)
            print(new_task)
            another_task_request = input("Task added. Create last task?")
            if another_task_request == "Y":
                another_task = input("Please enter your new task name: ")
                if another_task != "":
                    new_task_2 = ("Task 2:", another_task)
                    print(new_task_2)
                    print("Task Added")

    elif options == "Mark tasks as completed":
        print("Task 1:", new_task)
        print("Task 2", new_task_2)
        mark = input("Please enter the task you wish to mark: ")
        if mark == "Task 1":
            new_task = (new_task,": Completed")
            print("Task 1 is now reflecting:", new_task)

        elif mark == "Task 2":
            new_task_2 = (new_task_2,": Completed")
            print("Task 2 is now reflecting:", new_task_2)

    elif options == "View Tasks":
        print("Task 1:", new_task)
        print("Task 2:", new_task_2)

    elif options == "Delete Tasks":
        print("Task 1:", new_task)
        print("Task 2:", new_task_2)
        delete_task = input("Please enter the task you wish to delete: ")
        if delete_task == "Task 1":
            new_task = "No Task"
            delete_task_again = input("Task Deleted. Please visit (View Tasks) Would you like to delete another task?")
            if delete_task_again == "Y":
                new_task_2 = "No Task"
                print("Task Deleted. Please visit (View Tasks)")

    elif options == "Exit":
        print("Exiting")
        break
