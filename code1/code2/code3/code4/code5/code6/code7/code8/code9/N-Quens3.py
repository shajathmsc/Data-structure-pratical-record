def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def count_solutions(board, row, n):

    if row == n:
        return 1

    count = 0

    for col in range(n):

        if is_safe(board, row, col):
            board[row] = col

            count += count_solutions(board, row + 1, n)

            board[row] = -1

    return count


n = int(input("Enter number of Queens: "))

board = [-1] * n

total = count_solutions(board, 0, n)

print("\nNumber of Queens:", n)
print("Total Number of Solutions:", total)