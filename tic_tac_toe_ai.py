import math

def get_win_patterns(size):
    """Generate all winning patterns for an N x N grid."""
    patterns = []
    # Rows
    for i in range(size):
        patterns.append(tuple(range(i * size, (i + 1) * size)))
    # Columns
    for i in range(size):
        patterns.append(tuple(range(i, size * size, size)))
    # Diagonals
    patterns.append(tuple(range(0, size * size, size + 1)))
    patterns.append(tuple(range(size - 1, size * size - 1, size - 1)))
    return patterns

def check_winner(board, size):
    """Return the game result: 'X', 'O', 'Tie', or None."""
    win_patterns = get_win_patterns(size)
    for pattern in win_patterns:
        first = board[pattern[0]]
        if first != "-" and all(board[i] == first for i in pattern):
            return first
    if "-" not in board:
        return "Tie"
    return None

def evaluate(board, size):
    """Heuristic evaluation for depth-limited minimax."""
    # This is a simple heuristic: check for near-wins
    # For now, we'll stick to terminal states mostly, 
    # but we can return 0 if we hit depth limit.
    return 0

def minimax(board, size, depth, is_maximizing, alpha, beta, max_depth):
    w = check_winner(board, size)
    if w == "O": return 100 + depth
    if w == "X": return -100 - depth
    if w == "Tie": return 0
    if depth >= max_depth:
        return evaluate(board, size)

    if is_maximizing:
        best_score = -math.inf
        for i in range(size * size):
            if board[i] == "-":
                board[i] = "O"
                score = minimax(board, size, depth + 1, False, alpha, beta, max_depth)
                board[i] = "-"
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for i in range(size * size):
            if board[i] == "-":
                board[i] = "X"
                score = minimax(board, size, depth + 1, True, alpha, beta, max_depth)
                board[i] = "-"
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

def get_ai_move(board, size):
    """AI chooses best move using minimax with alpha-beta pruning."""
    best_score = -math.inf
    best_move = None
    
    # Adjust depth based on grid size for performance
    if size == 3:
        max_depth = 10
    elif size == 4:
        max_depth = 6
    else:
        max_depth = 4

    for i in range(size * size):
        if board[i] == "-":
            board[i] = "O"
            score = minimax(board, size, 0, False, -math.inf, math.inf, max_depth)
            board[i] = "-"
            if score > best_score:
                best_score = score
                best_move = i
    
    return best_move
