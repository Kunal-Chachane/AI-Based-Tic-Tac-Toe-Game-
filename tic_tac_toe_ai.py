import math
import random
from functools import lru_cache

AI_PLAYER = "O"
HUMAN_PLAYER = "X"
EMPTY_CELL = "-"
SEARCH_DEPTH_BY_SIZE = {3: 9, 4: 4, 5: 3}
RANDOM_MOVE_CHANCE = {"easy": 0.65, "medium": 0.25, "hard": 0.0}


@lru_cache(maxsize=None)
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
    
    return tuple(patterns)


def check_winner(board, size):
    """Check for a winner or a tie."""
    for pattern in get_win_patterns(size):
        first_mark = board[pattern[0]]
        if first_mark != EMPTY_CELL and all(board[index] == first_mark for index in pattern):
            return first_mark

    if EMPTY_CELL not in board:
        return "Tie"

    return None


def get_empty_cells(board):
    """Get indices of all empty cells."""
    return [index for index, value in enumerate(board) if value == EMPTY_CELL]


def evaluate_board(board, size):
    """Heuristic evaluation of the board for non-terminal states."""
    score = 0
    patterns = get_win_patterns(size)
    
    for pattern in patterns:
        line = [board[i] for i in pattern]
        ai_count = line.count(AI_PLAYER)
        human_count = line.count(HUMAN_PLAYER)
        
        if ai_count > 0 and human_count == 0:
            score += 10**ai_count
        elif human_count > 0 and ai_count == 0:
            score -= 10**human_count
            
    return score


def minimax(board, size, depth, is_maximizing, alpha, beta, max_depth):
    """Minimax algorithm with alpha-beta pruning."""
    winner = check_winner(board, size)
    
    if winner == AI_PLAYER:
        return 1000 - depth
    if winner == HUMAN_PLAYER:
        return depth - 1000
    if winner == "Tie":
        return 0
    if depth >= max_depth:
        return evaluate_board(board, size)

    empty_cells = get_empty_cells(board)

    if is_maximizing:
        best_score = -math.inf
        for move in empty_cells:
            board[move] = AI_PLAYER
            score = minimax(board, size, depth + 1, False, alpha, beta, max_depth)
            board[move] = EMPTY_CELL
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for move in empty_cells:
            board[move] = HUMAN_PLAYER
            score = minimax(board, size, depth + 1, True, alpha, beta, max_depth)
            board[move] = EMPTY_CELL
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score


def get_ai_move(board, size, difficulty="hard"):
    """Choose the best move for the AI based on difficulty."""
    empty_cells = get_empty_cells(board)
    if not empty_cells:
        return None

    # Difficulty handling
    difficulty_key = difficulty if difficulty in RANDOM_MOVE_CHANCE else "hard"
    if random.random() < RANDOM_MOVE_CHANCE[difficulty_key]:
        return random.choice(empty_cells)

    best_move = None
    best_score = -math.inf
    max_depth = SEARCH_DEPTH_BY_SIZE.get(size, 3)

    # For 3x3, we can do full search easily. For larger, we limit depth.
    for move in empty_cells:
        board[move] = AI_PLAYER
        score = minimax(board, size, 0, False, -math.inf, math.inf, max_depth)
        board[move] = EMPTY_CELL
        
        if score > best_score:
            best_score = score
            best_move = move
            
    return best_move
