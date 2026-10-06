MAX = 5
stack = []
top = -1

def push():
    global top

    if top == MAX - 1:
        print("Stack Overflow!")
    else:
        value = int(input("Enter the value: "))
        stack.append(value)
        top += 1
        print(value, "pushed into the stack.")


def pop():
    global top

    if top == -1:
        print("Stack Underflow!")
    else:
        value = stack.pop()
        top -= 1
        print(value, "popped from the stack.")


def peek():
    if top == -1:
        print("Stack is empty.")
    else:
        print("Top element is:", stack[top])


def display():
    if top == -1:
        print("Stack is empty.")
    else:
        print("Stack elements are:")
        for i in range(top, -1, -1):
            print(stack[i])


while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice!")
