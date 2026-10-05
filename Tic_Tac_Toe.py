def print_board(board):
    """Renders the 3x3 visual grid in the console."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    """Checks the 8 possible winning combinations for the current player."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    """Returns True if the board is full and no one has won."""
    return all(space in ["X", "O"] for space in board)

def play_game():
    """Manages the main game loop, player swapping, and input tracking."""
    # Initialize the board with position numbers 1-9
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    print("To make a move, enter a number from 1 to 9 corresponding to the grid position.")

    while not game_over:
        print_board(board)
        
        # Handle user input with built-in validation
        try:
            choice = int(input(f"Player {current_player}, choose your position (1-9): ")) - 1
            if choice < 0 or choice > 8:
                print("Invalid input! Please choose a number between 1 and 9.")
                continue
            if board[choice] in ["X", "O"]:
                print("That position is already taken! Try another one.")
                continue
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Place the player's marker on the board
        board[choice] = current_player

        # Check for endgame conditions
        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Congratulations! Player {current_player} wins! 🎉")
            game_over = True
        elif check_draw(board):
            print_board(board)
            print("🤝 It's a draw! Well played both.")
            game_over = True
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()