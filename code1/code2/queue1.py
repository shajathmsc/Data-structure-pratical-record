# Queue Implementation using Python List

queue = []

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        queue.append(value)
        print(value, "inserted into queue")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue Underflow")
        else:
            value = queue.pop(0)
            print(value, "deleted from queue")

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Queue elements:", queue)

    elif choice == 4:
        print("Program terminated")
        break

    else:
        print("Invalid choice")