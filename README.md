# Tic-Tac-Toe

A simple, interactive Tic-Tac-Toe game built using HTML, CSS, and Python. This project allows two players to play the classic Tic-Tac-Toe game in a web browser with a user-friendly interface.

## Features

- Two-player mode
- Real-time gameplay with user interaction
- Responsive UI with a simple design
- Winner determination logic
- CSS animations for smooth transitions

## Technologies Used

- **HTML**: Used for structuring the game board and UI elements.
- **CSS**: Used for styling the game board, buttons, and layout.
- **Python (Flask)**: Backend logic to handle game state and player moves.

##Usage

- Upon loading the game in your browser, two players can click on the empty cells to make their move.
- The game alternates between 'X' and 'O' after each move.
- The game detects and announces the winner when a player gets three marks in a row (horizontally, vertically, or diagonally).
- If the board is full without a winner, the game ends in a draw.

##File Structure

- index.html: The main HTML file containing the structure of the game board.
- style.css: The CSS file for styling the game elements.
- app.py: The Python Flask app that handles the game logic and routing.
- templates/: Folder containing the HTML files for Flask.
- static/: Folder containing the CSS and any static assets.


