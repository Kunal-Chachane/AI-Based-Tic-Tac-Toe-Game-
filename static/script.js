document.addEventListener('DOMContentLoaded', () => {
    const boardElement = document.getElementById('board');
    const statusText = document.getElementById('status-text');
    const statusCard = document.getElementById('status-card');
    const gridSizeSelect = document.getElementById('grid-size');
    const resetBtn = document.getElementById('reset');
    const modal = document.getElementById('winner-modal');
    const modalMsg = document.getElementById('winner-msg');
    const modalSub = document.getElementById('winner-sub');
    const modalIcon = document.getElementById('winner-icon');
    const playAgainBtn = document.getElementById('play-again');

    let size = parseInt(gridSizeSelect.value);
    let board = Array(size * size).fill("-");
    let gameActive = true;

    const createBoard = () => {
        boardElement.innerHTML = '';
        boardElement.className = `board size-${size}`;
        
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
            const val = board[index];
            if (val !== "-" && !cell.classList.contains('taken')) {
                cell.classList.add('taken', val.toLowerCase());
                cell.innerHTML = `<span>${val}</span>`;
            }
        });
    };

    const handleCellClick = async (e) => {
        const index = parseInt(e.target.dataset.index);

        if (board[index] !== "-" || !gameActive || statusCard.classList.contains('thinking')) return;

        // Player move
        board[index] = "X";
        updateUI();
        
        statusCard.classList.add('thinking');
        statusText.textContent = "AI is thinking...";

        try {
            const response = await fetch('/move', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ board, size }),
            });

            const data = await response.json();
            board = data.board;
            updateUI();

            if (data.winner) {
                showWinner(data.winner);
            } else {
                statusCard.classList.remove('thinking');
                statusText.textContent = "Your turn";
            }
        } catch (error) {
            console.error('Error:', error);
            statusText.textContent = "Connection error";
            statusCard.classList.remove('thinking');
        }
    };

    const showWinner = (winner) => {
        gameActive = false;
        statusCard.classList.remove('thinking');
        statusText.textContent = "Game Over";
        
        modal.classList.remove('hidden');
        if (winner === "Tie") {
            modalIcon.textContent = "🤝";
            modalMsg.textContent = "It's a Tie!";
            modalSub.textContent = "Great minds think alike.";
        } else if (winner === "X") {
            modalIcon.textContent = "🏆";
            modalMsg.textContent = "You Won!";
            modalSub.textContent = "You've outsmarted the AI!";
        } else {
            modalIcon.textContent = "🤖";
            modalMsg.textContent = "AI Won!";
            modalSub.textContent = "The machine is learning...";
        }
    };

    const resetGame = () => {
        size = parseInt(gridSizeSelect.value);
        board = Array(size * size).fill("-");
        gameActive = true;
        modal.classList.add('hidden');
        statusCard.classList.remove('thinking');
        statusText.textContent = "Your turn";
        createBoard();
    };

    gridSizeSelect.addEventListener('change', resetGame);
    resetBtn.addEventListener('click', resetGame);
    playAgainBtn.addEventListener('click', resetGame);

    // Initial setup
    createBoard();
});
