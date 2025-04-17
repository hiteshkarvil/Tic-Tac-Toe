Here is the python code for Tic-Tac-Toe Game

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Global game state
board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 board
current_player = "X"  # X starts the game
game_over = False  # Flag to check if the game is over

@app.route('/')
def index():
    return render_template('index.html', board=board)

@app.route('/play/<int:row>/<int:col>', methods=['POST'])
def play(row, col):
    global current_player, game_over

    # Check if the game is over
    if game_over:
        return jsonify({"error": "Game over. Please restart the game."})

    # Ensure the move is valid: the cell should be empty
    if board[row][col] != " ":
        return jsonify({"error": "Invalid move"})

    # Mark the cell with the current player's symbol
    board[row][col] = current_player

    # Check if there's a winner
    if check_winner(current_player):
        game_over = True
        return jsonify({"winner": current_player})

    # Check for a draw (no empty cells left)
    if is_draw():
        game_over = True
        return jsonify({"draw": True})

    # Switch player after the move
    current_player = "O" if current_player == "X" else "X"
    
    # Return the updated board
    return jsonify({"board": board})

@app.route('/reset', methods=['POST'])
def reset():
    global board, current_player, game_over
    board = [[" " for _ in range(3)] for _ in range(3)]  # Reset board
    current_player = "X"  # X starts the game again
    game_over = False  # Reset game over flag
    return jsonify({"board": board})

# Check if the current player wins
def check_winner(player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Column
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # Diagonal
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  # Opposite Diagonal
        return True
    return False

# Check if the game is a draw
def is_draw():
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

if __name__ == '__main__':
    app.run(debug=True)
