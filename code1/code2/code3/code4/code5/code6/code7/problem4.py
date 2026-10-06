n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

capacity = int(input("Enter capacity: "))

dp = [[0] * (capacity + 1) for _ in range(n + 1)]


for i in range(1, n + 1):

    for w in range(1, capacity + 1):

        if weights[i - 1] <= w:

            dp[i][w] = max(
                values[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )

        else:

            dp[i][w] = dp[i - 1][w]


# Find selected items
w = capacity
selected = []

for i in range(n, 0, -1):

    if dp[i][w] != dp[i - 1][w]:

        selected.append(i)
        w -= weights[i - 1]


print("Maximum value:", dp[n][capacity])

print("Selected items:", selected[::-1])