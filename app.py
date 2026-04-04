from flask import Flask, render_template, request, jsonify
from tic_tac_toe_ai import check_winner, get_ai_move

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/move", methods=["POST"])
def move():
    data = request.get_json(silent=True) or {}
    size = int(data.get("size", 3))
    board = data.get("board") or []
    difficulty = data.get("difficulty", "hard")

    if len(board) != size * size:
        return jsonify({"error": "Invalid board"}), 400

    winner = check_winner(board, size)
    if winner:
        return jsonify({"board": board, "winner": winner})

    move_index = get_ai_move(board, size, difficulty)
    if move_index is not None:
        board[move_index] = "O"

    winner = check_winner(board, size)
    return jsonify({"board": board, "winner": winner})


if __name__ == "__main__":
    app.run(debug=True)
