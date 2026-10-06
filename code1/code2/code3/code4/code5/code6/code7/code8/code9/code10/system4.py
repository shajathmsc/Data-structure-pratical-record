def assign_jobs(cost, row, used, current, assignment, best):

    n = len(cost)

    if row == n:
        if current < best[0]:
            best[0] = current
            best[1] = assignment[:]
        return

    for job in range(n):

        if not used[job]:

            total = current + cost[row][job]

            if total < best[0]:

                used[job] = True
                assignment[row] = job

                assign_jobs(
                    cost,
                    row + 1,
                    used,
                    total,
                    assignment,
                    best
                )

                used[job] = False


n = int(input("Enter number of Employees: "))

names = []

for i in range(n):
    name = input("Enter Employee Name: ")
    names.append(name)

cost = []

print("\nEnter Cost Matrix:")

for i in range(n):
    cost.append(list(map(int, input().split())))

used = [False] * n
assignment = [-1] * n
best = [float("inf"), None]

assign_jobs(cost, 0, used, 0, assignment, best)

print("\n--- Final Job Allocation ---")

for i in range(n):
    print(
        names[i],
        "-> Job",
        best[1][i] + 1,
        "Cost =",
        cost[i][best[1][i]]
    )

print("\nMinimum Total Cost:", best[0])