def task():
    tasks = []
    print("Welcome to your To-Do List!")

    try:
        total_tasks = int(input("How many tasks do you want to add? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print("\nToday's tasks:")
    for t in tasks:
        print(f"- {t}")

    while True:
        try:
            operation = int(input("\nEnter:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if operation == 1:
            new_task = input("Enter the new task: ")
            tasks.append(new_task)
            print(f"Task '{new_task}' added successfully!")

        elif operation == 2:
            updated_val = input("Enter the task you want to update: ")
            if updated_val in tasks:
                new_val = input("Enter the new task: ")
                index = tasks.index(updated_val)
                tasks[index] = new_val
                print(f"Task updated successfully!")
            else:
                print("Task not found.")

        elif operation == 3:
            del_val = input("Enter the task you want to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' deleted successfully!")
            else:
                print("Task not found.")

        elif operation == 4:
            if not tasks:
                print("No tasks available.")
            else:
                print("\nToday's tasks:")
                for t in tasks:
                    print(f"- {t}")

        elif operation == 5:
            print("Exiting the To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

#task()