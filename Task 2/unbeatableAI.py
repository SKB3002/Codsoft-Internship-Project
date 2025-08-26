import math

# Initialize board
board = [" " for _ in range(9)]

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def is_winner(board, player):
    winning_combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in winning_combos)

def is_full(board):
    return " " not in board

def minimax(board, depth, is_maximizing):
    if is_winner(board, "O"):
        return 1
    elif is_winner(board, "X"):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:  # AI's turn
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth+1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:  # Human's turn
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth+1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Game loop
while True:
    # reset board at the start of each game
    board = [" " for _ in range(9)]

    while True:
        print_board(board)

        # Human move
        human_move = int(input("Enter your move (1-9): ")) - 1
        if board[human_move] != " ":
            print("Invalid move! Try again.")
            continue
        board[human_move] = "X"

        if is_winner(board, "X"):
            print_board(board)
            print("You win!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        ai_move = best_move(board)
        board[ai_move] = "O"

        if is_winner(board, "O"):
            print_board(board)
            print("AI wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

    # Replay option
    replay = input("Play again? (y/n): ").lower()
    if replay != "y":
        print("Thanks for playing!")
        break
