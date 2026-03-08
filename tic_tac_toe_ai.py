# Tic-Tac-Toe with Minimax AI 

board = ["-"] * 9

def show():
    """Display the current board."""
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    print()


def winner():
    """Return the game result: 'X', 'O', 'Tie', or None."""
    win_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_patterns:
        if board[a] == board[b] == board[c] != "-":
            return board[a]
    if "-" not in board:
        return "Tie"
    return None


def minimax(ai_turn):
    """Minimax algorithm to find optimal move."""
    w = winner()

    if w == "O": return 1
    if w == "X": return -1
    if w == "Tie": return 0

    scores = []
    for i in range(9):
        if board[i] == "-":
            board[i] = "O" if ai_turn else "X"
            score = minimax(not ai_turn)
            board[i] = "-"
            scores.append(score)

    return max(scores) if ai_turn else min(scores)


def ai_move():
    """AI chooses best move using minimax."""
    best_score = -10
    best_move = None

    for i in range(9):
        if board[i] == "-":
            board[i] = "O"
            score = minimax(False)
            board[i] = "-"
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


show()

while True:
    try:
        p = int(input("Enter 1-9: ")) - 1
        if p not in range(9):
            print("Choose a number from 1 to 9.")
            continue
        if board[p] != "-":
            print("That spot is taken.")
            continue
        board[p] = "X"
    except ValueError:
        print("Enter a valid number.")
        continue

    show()
    if winner():
        break

    ai_move()
    print("AI move:")
    show()
    if winner():
        break

result = winner()

if result == "X":
    print("Result: Player wins!")
elif result == "O":
    print("Result: AI wins!")
else:
    print("Result: Tie game.")