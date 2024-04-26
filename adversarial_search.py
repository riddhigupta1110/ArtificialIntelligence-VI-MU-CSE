import math
EMPTY = 0
PLAYER_X = 1
PLAYER_O = -1

def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return 0  # No winner

def game_over(board):
    # Check for a win or if the board is full
    return evaluate(board) != 0 or all(board[i][j] != EMPTY for i in range(3) for j in range(3))

def possible_moves(board):
    # Generate all possible moves (empty cells)
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def make_move(board, move, player):
    # Apply the move to the board
    i, j = move
    new_board = [row[:] for row in board]
    new_board[i][j] = player
    return new_board

def minimax(board, depth, maximizing_player):
    if depth == 0 or game_over(board):
        return evaluate(board)

    if maximizing_player:
        max_eval = -math.inf
        for move in possible_moves(board):
            new_board = make_move(board, move, PLAYER_X)
            eval = minimax(new_board, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in possible_moves(board):
            new_board = make_move(board, move, PLAYER_O)
            eval = minimax(new_board, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_move = None
    max_eval = -math.inf
    for move in possible_moves(board):
        new_board = make_move(board, move, PLAYER_X)
        eval = minimax(new_board, 8, False)  # Adjust depth as needed
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move

# Display the board nicely
def display_board(board):
    for row in board:
        print(" | ".join(map(lambda x: "X" if x == PLAYER_X else ("O" if x == PLAYER_O else " "), row)))
        print("-" * 9)

# Example usage
board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

print("Welcome to Tic-Tac-Toe!\n")
print("The positions are represented as follows:")
print(" 1 | 2 | 3 ")
print("-----------")
print(" 4 | 5 | 6 ")
print("-----------")
print(" 7 | 8 | 9 \n")

print("Player plays with 'O', AI plays with 'X'\n")

display_board(board)

while not game_over(board):
    print("\nPlayer's Turn:")
    move = int(input("Enter your move (1-9): ")) - 1
    x, y = move // 3, move % 3
    if board[x][y] != EMPTY:
        print("Invalid move, try again.")
        continue
    board[x][y] = PLAYER_O
    display_board(board)
    if game_over(board):
        break

    print("\nAI's Choices:")
    for i, move in enumerate(possible_moves(board), start=1):
        new_board = make_move(board, move, PLAYER_X)
        eval_score = minimax(new_board, 8, False)  # Adjust depth as needed
        print(f"{i}. Row: {move[0] + 1}, Column: {move[1] + 1} - Evaluation Score: {eval_score}")
    
    print("\nAI's Turn:")
    ai_move = find_best_move(board)
    print(f"AI chooses to place 'X' at row {ai_move[0] + 1}, column {ai_move[1] + 1}")
    board[ai_move[0]][ai_move[1]] = PLAYER_X
    display_board(board)
    print("==============================")

winner = evaluate(board)
if winner == PLAYER_X:
    print("\nAI wins!")
elif winner == PLAYER_O:
    print("\nPlayer wins!")
else:
    print("\nIt's a draw!")