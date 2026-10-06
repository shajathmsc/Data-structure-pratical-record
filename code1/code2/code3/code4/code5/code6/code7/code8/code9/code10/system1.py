def calculate_cost(cost, assignment, n):
    total = 0

    for employee in range(n):
        task = assignment[employee]
        total += cost[employee][task]

    return total


def branch_and_bound(cost, employee, n, assignment, used, best):
    if employee == n:
        current_cost = calculate_cost(cost, assignment, n)

        if current_cost < best[0]:
            best[0] = current_cost
            best[1] = assignment[:]

        return

    for task in range(n):

        if not used[task]:
            assignment[employee] = task
            used[task] = True

            current_cost = 0

            for i in range(employee + 1):
                current_cost += cost[i][assignment[i]]

            if current_cost < best[0]:
                branch_and_bound(
                    cost,
                    employee + 1,
                    n,
                    assignment,
                    used,
                    best
                )

            used[task] = False
            assignment[employee] = -1


n = int(input("Enter number of employees/tasks: "))

cost = []

print("\nEnter the cost matrix:")

for i in range(n):
    row = list(map(int, input(
        "Enter costs for Employee " + str(i + 1) + ": "
    ).split()))

    cost.append(row)

assignment = [-1] * n
used = [False] * n

best = [float("inf"), None]

branch_and_bound(
    cost,
    0,
    n,
    assignment,
    used,
    best
)

print("\n--- Optimal Job Allocation ---")

for employee in range(n):
    print(
        "Employee", employee + 1,
        "-> Task", best[1][employee],
        "Cost =", cost[employee][best[1][employee]]
    )

print("\nMinimum Total Cost:", best[0])