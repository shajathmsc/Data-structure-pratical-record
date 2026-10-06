def allocate(cost, row, selected, used, current, best):
    n = len(cost)

    if row == n:
        if current < best[0]:
            best[0] = current
            best[1] = selected[:]
        return

    for col in range(n):

        if not used[col]:

            new_cost = current + cost[row][col]

            if new_cost < best[0]:

                used[col] = True
                selected[row] = col

                allocate(
                    cost,
                    row + 1,
                    selected,
                    used,
                    new_cost,
                    best
                )

                used[col] = False


n = int(input("Enter number of Employees: "))

cost = []

for i in range(n):
    print("Enter task costs for Employee", i + 1)
    cost.append(list(map(int, input().split())))

selected = [-1] * n
used = [False] * n
best = [float("inf"), None]

allocate(cost, 0, selected, used, 0, best)

print("\n--- Task Allocation ---")

for i in range(n):
    print(
        "Employee", i + 1,
        "assigned to Task", best[1][i] + 1,
        "Cost =", cost[i][best[1][i]]
    )

print("Minimum Cost =", best[0])