def solve(cost, employee, used, total, assignment, best):

    n = len(cost)

    if employee == n:
        if total < best["cost"]:
            best["cost"] = total
            best["assignment"] = assignment[:]
        return

    for job in range(n):

        if used[job] == False:

            new_total = total + cost[employee][job]

            # Branch and Bound
            if new_total < best["cost"]:

                used[job] = True
                assignment[employee] = job

                solve(
                    cost,
                    employee + 1,
                    used,
                    new_total,
                    assignment,
                    best
                )

                used[job] = False


n = int(input("Enter number of Employees: "))

cost = []

print("Enter Cost Matrix:")

for i in range(n):
    cost.append(list(map(int, input().split())))

used = [False] * n
assignment = [-1] * n

best = {
    "cost": float("inf"),
    "assignment": None
}

solve(cost, 0, used, 0, assignment, best)

print("\nMinimum Cost:", best["cost"])

print("\nAssignment:")

for i in range(n):
    job = best["assignment"][i]
    print(
        "Employee", i + 1,
        "-> Job", job + 1
    )