def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(board, row + 1, n, solutions)
            board[row] = -1


def display_solution(solution, n):
    for row in solution:
        for col in range(n):
            if row == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


n = int(input("Enter number of Queens: "))

board = [-1] * n
solutions = []

solve_n_queens(board, 0, n, solutions)

print("\nTotal Solutions:", len(solutions))

for i, solution in enumerate(solutions, 1):
    print("\nSolution", i)
    display_solution(solution, n)