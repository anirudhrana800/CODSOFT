import tkinter as tk
from tkinter import messagebox

# Initialize the game board
board = [['' for _ in range(3)] for _ in range(3)
         ]
current_player = 'X'
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create the game board GUI
buttons = [[None for _ in range(3)] for _ in range(3)]


def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    if all(board[i][j] != '' for i in range(3) for j in range(3)):
        return 'tie'
    return None


def on_button_click(i, j):
    global current_player
    if board[i][j] == '' and not check_winner():
        board[i][j] = current_player
        buttons[i][j].config(text=current_player)
        winner = check_winner()
        if winner:
            if winner == 'tie':
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            else:
                messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
            root.quit()
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            if current_player == 'O':
                ai_move()


def ai_move():
    best_score = -float('inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ''
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    if best_move:
        i, j = best_move
        on_button_click(i, j)


def minimax(board, depth, is_maximizing):
    result = check_winner()
    if result:
        if result == 'O':
            return 1
        elif result == 'X':
            return -1
        else:
            return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ''
                    best_score = min(score, best_score)
        return best_score


for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', width=10, height=3, command=lambda i=i, j=j: on_button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
