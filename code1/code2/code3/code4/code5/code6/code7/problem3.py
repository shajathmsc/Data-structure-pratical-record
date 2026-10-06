def knapsack(weights, values, capacity, n, memo):

    if n == 0 or capacity == 0:
        return 0

    if (n, capacity) in memo:
        return memo[(n, capacity)]

    if weights[n - 1] <= capacity:

        include = values[n - 1] + knapsack(
            weights,
            values,
            capacity - weights[n - 1],
            n - 1,
            memo
        )

        exclude = knapsack(
            weights,
            values,
            capacity,
            n - 1,
            memo
        )

        result = max(include, exclude)

    else:

        result = knapsack(
            weights,
            values,
            capacity,
            n - 1,
            memo
        )

    memo[(n, capacity)] = result

    return result


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]

capacity = int(input("Enter capacity: "))

memo = {}

result = knapsack(
    weights,
    values,
    capacity,
    len(weights),
    memo
)

print("Maximum value:", result)