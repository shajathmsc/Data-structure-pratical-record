def is_safe(board, row, col, n):

    for i in range(row):
        if board[i][col] == 1:
            return False

    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):
    if row == n:
        print_board(board, n)
        return 1

    count = 0

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            count += solve(board, row + 1, n)

            board[row][col] = 0

    return count


def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


n = int(input("Enter number of Queens: "))

board = [[0 for j in range(n)] for i in range(n)]

total = solve(board, 0, n)

print("Total Solutions:", total)