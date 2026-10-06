# Max Heap Implementation

class MaxHeap:

    def __init__(self):
        self.heap = []

    # Insert element
    def insert(self, value):
        self.heap.append(value)

        index = len(self.heap) - 1

        # Heapify Up
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = \
                    self.heap[parent], self.heap[index]

                index = parent
            else:
                break

    # Delete root element
    def delete(self):
        if len(self.heap) == 0:
            print("Heap is empty")
            return

        root = self.heap[0]

        last = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last

            index = 0

            # Heapify Down
            while True:
                left = 2 * index + 1
                right = 2 * index + 2
                largest = index

                if (left < len(self.heap) and
                        self.heap[left] > self.heap[largest]):
                    largest = left

                if (right < len(self.heap) and
                        self.heap[right] > self.heap[largest]):
                    largest = right

                if largest != index:
                    self.heap[index], self.heap[largest] = \
                        self.heap[largest], self.heap[index]

                    index = largest
                else:
                    break

        print(root, "deleted from heap")

    # Display heap
    def display(self):
        print("Heap:", self.heap)


# Create heap
h = MaxHeap()

while True:

    print("\n--- MAX HEAP MENU ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        h.insert(value)
        print(value, "inserted into heap")

    elif choice == 2:
        h.delete()

    elif choice == 3:
        h.display()

    elif choice == 4:
        print("Program terminated")
        break

    else:
        print("Invalid choice")