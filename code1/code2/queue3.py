queue = []

while True:
    print("\n--- PRIORITY QUEUE ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        priority = int(input("Enter priority: "))

        queue.append((priority, value))
        queue.sort()

        print(value, "inserted with priority", priority)

    elif choice == 2:
        if len(queue) == 0:
            print("Priority Queue is empty")
        else:
            priority, value = queue.pop(0)
            print(value, "deleted")

    elif choice == 3:
        if len(queue) == 0:
            print("Priority Queue is empty")
        else:
            print("Priority Queue:")
            for priority, value in queue:
                print("Element:", value, "Priority:", priority)

    elif choice == 4:
        break

    else:
        print("Invalid choice")