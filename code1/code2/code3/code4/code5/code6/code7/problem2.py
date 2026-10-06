items = []

n = int(input("Enter number of items: "))

for i in range(n):

    weight = int(input("Enter weight: "))
    value = int(input("Enter value: "))

    ratio = value / weight

    items.append((ratio, weight, value))


capacity = int(input("Enter knapsack capacity: "))

# Sort by value/weight ratio
items.sort(reverse=True)

total_value = 0

for ratio, weight, value in items:

    if capacity >= weight:

        capacity -= weight
        total_value += value

    else:

        total_value += ratio * capacity
        capacity = 0
        break


print("Maximum value:", total_value)