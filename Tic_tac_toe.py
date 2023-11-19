def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 13)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Check columns
    for col in range(len(board)):
        if all(board[row][col] == board[row - 1][col] != ' ' for row in range(1, len(board))):
            return True

    # Check diagonals
    if all(board[i][i] == board[i - 1][i - 1] != ' ' for i in range(1, len(board))) or \
            all(board[i][len(board) - 1 - i] == board[i - 1][len(board) - i] != ' ' for i in range(1, len(board))):
        return True

    return False

def is_board_full(board):
    return all(board[row][col] != ' ' for row in range(len(board)) for col in range(len(board[0])))

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
