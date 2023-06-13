import random
import tkinter as tk
from tkinter import messagebox

def print_board(board):
    print("---------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(board[i][j], end="|")
        print("\n---------")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    return empty_cells

def make_move(board, player, row, col):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        return False

def on_button_click(row, col):
    global board, player, game_over, buttons

    if game_over:
        return

    if make_move(board, player, row, col):
        buttons[row][col].config(text=player)
        if check_win(board, player):
            messagebox.showinfo("Game Over", f"{player} wins!")
            game_over = True
        elif len(get_empty_cells(board)) == 0:
            messagebox.showinfo("Game Over", "It's a tie!")
            game_over = True
        player = "O" if player == "X" else "X"
        if not game_over and player == "O":
            empty_cells = get_empty_cells(board)
            cell = random.choice(empty_cells)
            make_move(board, player, cell[0], cell[1])
            buttons[cell[0]][cell[1]].config(text=player)
            if check_win(board, player):
                messagebox.showinfo("Game Over", f"{player} wins!")
                game_over = True
            elif len(get_empty_cells(board)) == 0:
                messagebox.showinfo("Game Over", "It's a tie!")
                game_over = True
            player = "X" if player == "O" else "O"

def create_board_buttons(root):
    buttons = []
    for i in range(3):
        row = []
        for j in range(3):
            button = tk.Button(root, text=" ", font=("Helvetica", 20), width=4, height=2,
                               command=lambda row=i, col=j: on_button_click(row, col))
            button.grid(row=i, column=j)
            row.append(button)
        buttons.append(row)
    return buttons

def create_new_game():
    global board, player, game_over, buttons
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
            buttons[i][j].config(text=" ")
    player = "X"
    game_over = False

def create_gui():
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    buttons = create_board_buttons(root)
    new_game_button = tk.Button(root, text="New Game", font=("Helvetica", 14), command=create_new_game)
    new_game_button.grid(row=3, column=0, columnspan=3, pady=10)
    return root, buttons

def play_game():
    global board, player, game_over, buttons

    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"
    game_over = False

    root, buttons = create_gui()
    root.mainloop()

play_game()
