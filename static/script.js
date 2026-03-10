document.addEventListener('DOMContentLoaded', () => {
    const boardElement = document.getElementById('board');
    const statusElement = document.getElementById('status');
    const resetButton = document.getElementById('reset');
    const gridSizeSelect = document.getElementById('grid-size');

    let size = parseInt(gridSizeSelect.value);
    let board = Array(size * size).fill("-");
    let gameActive = true;

    const createBoard = () => {
        boardElement.innerHTML = '';
        document.documentElement.style.setProperty('--grid-size', size);
        
        for (let i = 0; i < size * size; i++) {
            const cell = document.createElement('div');
            cell.classList.add('cell');
            cell.dataset.index = i;
            cell.addEventListener('click', handleCellClick);
            boardElement.appendChild(cell);
        }
    };

    const updateUI = () => {
        const cells = document.querySelectorAll('.cell');
        cells.forEach((cell, index) => {
            cell.textContent = board[index] === "-" ? "" : board[index];
            cell.classList.remove('x', 'o', 'taken');
            if (board[index] !== "-") {
                cell.classList.add(board[index].toLowerCase());
                cell.classList.add('taken');
            }
        });
    };

    const handleCellClick = async (e) => {
        const index = parseInt(e.target.dataset.index);

        if (board[index] !== "-" || !gameActive) return;

        // Player move
        board[index] = "X";
        updateUI();
        statusElement.textContent = "AI is thinking...";

        try {
            const response = await fetch('/move', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ board, size }),
            });

            const data = await response.json();
            board = data.board;
            updateUI();

            if (data.winner) {
                gameActive = false;
                if (data.winner === "Tie") {
                    statusElement.textContent = "It's a Tie!";
                } else {
                    statusElement.textContent = `${data.winner} Wins!`;
                }
            } else {
                statusElement.textContent = "Your turn (X)";
            }
        } catch (error) {
            console.error('Error:', error);
            statusElement.textContent = "Error connecting to server.";
        }
    };

    const resetGame = () => {
        size = parseInt(gridSizeSelect.value);
        board = Array(size * size).fill("-");
        gameActive = true;
        createBoard();
        statusElement.textContent = "Your turn (X)";
    };

    gridSizeSelect.addEventListener('change', resetGame);
    resetButton.addEventListener('click', resetGame);

    // Initial setup
    createBoard();
});
