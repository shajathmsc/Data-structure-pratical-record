# 0/1 Knapsack using Dynamic Programming

n = int(input("Enter number of items: "))

weights = []
values = []

print("Enter weights of the items:")

for i in range(n):
    w = int(input("Weight of item " + str(i + 1) + ": "))
    weights.append(w)

print("\nEnter values of the items:")

for i in range(n):
    v = int(input("Value of item " + str(i + 1) + ": "))
    values.append(v)

capacity = int(input("\nEnter knapsack capacity: "))

# Create DP table
dp = [[0 for j in range(capacity + 1)]
      for i in range(n + 1)]


# Fill DP table
for i in range(1, n + 1):

    for w in range(1, capacity + 1):

        if weights[i - 1] <= w:

            dp[i][w] = max(
                values[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )

        else:
            dp[i][w] = dp[i - 1][w]


# Display maximum value
print("\nMaximum value:", dp[n][capacity])


# Find selected items
w = capacity
selected = []

for i in range(n, 0, -1):

    if dp[i][w] != dp[i - 1][w]:

        selected.append(i)
        w = w - weights[i - 1]


print("Selected items:", selected[::-1])