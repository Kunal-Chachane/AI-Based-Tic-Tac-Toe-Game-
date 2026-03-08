<<<<<<< HEAD
# AI-Based-Tic-Tac-Toe-Game-
• Problem: Intelligent game opponent • Feasibility Study: Limited state space • AI Technique(s): Minimax, Alpha-Beta Pruning • Representation: Game tree • Tools: Python • Outcome: Optimal gameplay comparison
=======
# AI Tic-Tac-Toe (Minimax & Alpha-Beta Pruning)

This project implements an optimal AI opponent for Tic-Tac-Toe using classical search algorithms.

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
If at any point Beta becomes less than or equal to Alpha, the maximizer doesn't need to look at the rest of that branch because the minimizer already has a better option elsewhere.

### 3. Game Tree
The "Game Tree" represents all possible states of the game.
- **Nodes**: Represent a board state.
- **Edges**: Represent a valid move.
- **Leaves**: Represent terminal states (Win/Loss/Draw).
For Tic-Tac-Toe, the full tree has 9! (362,880) possible move sequences, though many are redundant.

## Performance Improvement
By using Alpha-Beta pruning, the AI explores significantly fewer nodes while still finding the same "optimal" move. In the early game, you will see node counts drop from thousands to hundreds, making the AI's "thinking" phase much faster.

## How to Run
Ensure you have Python 3 installed. Run the script using:
```bash
python tic_tac_toe_ai.py
```
>>>>>>> 0d34dd5 (Initial commit - AI Powered Tic Tac Toe Game)
