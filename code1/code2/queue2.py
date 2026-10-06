# Circular Queue Implementation

SIZE = 5

queue = [None] * SIZE

front = -1
rear = -1


def enqueue():
    global front, rear

    value = int(input("Enter element: "))

    # Check whether queue is full
    if (rear + 1) % SIZE == front:
        print("Circular Queue is Full")
        return

    # First element
    if front == -1:
        front = 0
        rear = 0
    else:
        rear = (rear + 1) % SIZE

    queue[rear] = value

    print(value, "inserted into circular queue")


def dequeue():
    global front, rear

    # Check whether queue is empty
    if front == -1:
        print("Circular Queue is Empty")
        return

    value = queue[front]
    queue[front] = None

    # Only one element
    if front == rear:
        front = -1
        rear = -1
    else:
        front = (front + 1) % SIZE

    print(value, "deleted from circular queue")


def display():
    if front == -1:
        print("Circular Queue is Empty")
        return

    print("Circular Queue elements:")

    i = front

    while True:
        print(queue[i], end=" ")

        if i == rear:
            break

        i = (i + 1) % SIZE

    print()


while True:

    print("\n--- CIRCULAR QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Program terminated")
        break

    else:
        print("Invalid choice")