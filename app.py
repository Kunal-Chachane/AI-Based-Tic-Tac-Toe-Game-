from flask import Flask, render_template, request, jsonify
from tic_tac_toe_ai import check_winner, get_ai_move

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    board = data.get("board")
    size = int(data.get("size", 3))
    
    # Check if game is already over
    winner = check_winner(board, size)
    if winner:
        return jsonify({"board": board, "winner": winner})

    # AI move
    move_index = get_ai_move(board, size)
    if move_index is not None:
        board[move_index] = "O"
    
    winner = check_winner(board, size)
    return jsonify({"board": board, "winner": winner})

if __name__ == "__main__":
    app.run(debug=True)
