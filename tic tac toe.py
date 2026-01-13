import random
board = [" " for _ in range(9)]
def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()
def check_winner(player):
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),   # rows
        (0,3,6), (1,4,7), (2,5,8),   # columns
        (0,4,8), (2,4,6)             # diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False
def is_draw():
    return " " not in board
def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")
def ai_move():
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)
    board[move] = "O"
print("TIC TAC TOE 🎮 Human (X) vs AI (O)")
print("Positions are numbered 1 to 9")
print_board()
while True:
    human_move()
    print_board()
    if check_winner("X"):
        print("You win! 🎉")
        break
    if is_draw():
        print("It's a draw!")
        break
    ai_move()
    print("AI played:")
    print_board()
    if check_winner("O"):
        print("AI wins! 🤖")
        break
    if is_draw():
        print("It's a draw!")
        break
