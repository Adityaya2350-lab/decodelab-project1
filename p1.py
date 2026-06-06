tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add a task") 
    print("2. View tasks")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
    elif choice == "2":
        print("\n--- Tasks ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")