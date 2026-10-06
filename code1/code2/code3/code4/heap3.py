import heapq

heap = []

while True:

    print("\n--- MIN HEAP ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        heapq.heappush(heap, value)
        print(value, "inserted")

    elif choice == 2:
        if len(heap) == 0:
            print("Heap is empty")
        else:
            value = heapq.heappop(heap)
            print(value, "deleted")

    elif choice == 3:
        print("Heap:", heap)

    elif choice == 4:
        break

    else:
        print("Invalid choice")