import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if any player has won
def check_winner(board, player):
    for i in range(3):
        # Check rows and columns
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, "O"):
        return 1
    elif check_winner(board, "X"):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

# Function to find the best move for AI
def find_best_move(board):
    best_move = None
    best_score = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Main function to play Tic-Tac-Toe
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human_turn = True

    while True:
        print_board(board)
        if check_winner(board, "X"):
            print("You win!")
            break
        elif check_winner(board, "O"):
            print("AI wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        if human_turn:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] == " ":
                board[row][col] = "X"
                human_turn = False
            else:
                print("Cell already taken. Try again.")
        else:
            print("AI is making a move...")
            row, col = find_best_move(board)
            board[row][col] = "O"
            human_turn = True

play_game()
