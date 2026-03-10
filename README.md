# AI Tic-Tac-Toe (Minimax & Alpha-Beta Pruning)

This project implements an optimal AI opponent for Tic-Tac-Toe using classical search algorithms.

## Features
- **Minimax AI**: An unbeatable AI opponent that evaluates all possible moves.
- **Web Interface**: A modern, interactive web-based game.
- **CLI Interface**: The original command-line version of the game.

## Web Version (New)

The project now includes a modern web interface built with Flask and Vanilla CSS.

### Prerequisites
- Python 3.x
- Flask (`pip install flask`)

### Running the Web App
1. Install Flask:
   ```bash
   pip install flask
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to `http://127.0.0.1:5000`

## CLI Version
You can still run the original command-line version:
```bash
python tic_tac_toe_ai.py
```

## Algorithms Explained

### 1. Minimax Algorithm
Minimax is a recursive decision-making algorithm used in two-player games. 
- **Maximizer**: Tries to get the highest score possible.
- **Minimizer**: Tries to get the lowest score possible.
In Tic-Tac-Toe, the AI (Maximizer) evaluates every possible move until the end of the game (win, loss, or draw). It assumes the human (Minimizer) will also play optimally.

### 2. Alpha-Beta Pruning
Alpha-Beta pruning is an optimization for Minimax. It reduces the number of nodes evaluated in the search tree by "pruning" branches that cannot possibly influence the final decision.
- **Alpha**: The best value the maximizer is guaranteed.
- **Beta**: The best value the minimizer is guaranteed.

### 3. Game Tree
The "Game Tree" represents all possible states of the game.
- **Nodes**: Represent a board state.
- **Edges**: Represent a valid move.
- **Leaves**: Represent terminal states (Win/Loss/Draw).
