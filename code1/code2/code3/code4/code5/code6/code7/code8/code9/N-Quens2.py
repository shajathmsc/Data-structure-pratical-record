def is_safe(board, row, col, n):

    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row, n):

    if row == n:
        return True

    for col in range(n):

        if is_safe(board, row, col, n):
            board[row] = col

            if solve(board, row + 1, n):
                return True

            board[row] = -1

    return False


def display(board, n):

    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


n = int(input("Enter number of Queens: "))

board = [-1] * n

if solve(board, 0, n):
    print("\nOne Possible Solution:")
    display(board, n)
else:
    print("No solution exists")