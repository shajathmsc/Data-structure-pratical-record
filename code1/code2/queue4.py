queue = []

while True:
    print("\n--- CUSTOMER SERVICE QUEUE ---")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. Show Waiting Customers")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter customer name: ")
        queue.append(name)
        print(name, "added to the queue")

    elif choice == 2:
        if len(queue) == 0:
            print("No customers waiting")
        else:
            customer = queue.pop(0)
            print("Serving customer:", customer)

    elif choice == 3:
        if len(queue) == 0:
            print("No customers waiting")
        else:
            print("Waiting Customers:")
            for customer in queue:
                print(customer)

    elif choice == 4:
        print("Program terminated")
        break

    else:
        print("Invalid choice")