def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1
    return True

def solve_nqueens(board, row, n):
    if row >= n:
        return True
    if any(board[row]):
        return solve_nqueens(board, row + 1, n)
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_nqueens(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtrack
    return False

def n_queens_with_first_queen(n, first_row, first_col):
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[first_row][first_col] = 1
    if not solve_nqueens(board, 0, n):
        print("Solution does not exist with first queen at position:", (first_row, first_col))
    else:
        print("Final N-Queens Board:")
        print_board(board)

if __name__ == "__main__":
    n = 8  # Size of the board
    first_row = 0  # First queen's row
    first_col = 0  # First queen's column
    print(f"Solving {n}-Queens with first queen at ({first_row}, {first_col}):")
    n_queens_with_first_queen(n, first_row, first_col)
