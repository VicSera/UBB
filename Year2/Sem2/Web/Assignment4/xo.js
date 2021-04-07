state = {
    board: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    turn: 1,
    disabled: false
};

const COMPUTER = 2;
const PLAYER = 1;

function nextTurn() {
    state.turn = 2 - state.turn + 1;

    if (state.turn === COMPUTER) {
        const bestMove = getBestMove(state.board);
        console.log(bestMove);
        cellClicked(bestMove.move);
    }
}

function updateCell(index) {
    const playerTurn = state.turn === PLAYER ? "x" : "o";
    document.getElementById("board").children[index]
        .classList.add(playerTurn);

    const evaluation = evaluateState(state.board);
    if (evaluation.winner !== 0) {
        document.getElementById("turn").textContent =
            "Winner: " + (evaluation.winner === COMPUTER? "Computer" : "Player");
        state.disabled = true;
        highlightCells(evaluation.winnerSquares);
        disableCells();
    }
    else if (!movesRemaining(state.board)) {
        document.getElementById("turn").textContent = "It's a tie!";
        state.disabled = true;
        disableCells();
    }
    else
        document.getElementById("turn").textContent = "Next move: " + playerTurn.toUpperCase();
}

function disableCells() {
    for (const child of document.getElementById("board").children)
        child.classList.add("disabled");
}

function highlightCells(indices) {
    for (const index of indices) {
        document.getElementById("board").children[index]
            .classList.add("winnerCell");
    }
}

function cellClicked(index) {
    if (state.disabled || state.board[index] !== 0)
        return;

    state.board[index] = state.turn;
    updateCell(index);

    nextTurn();
}

function clearBoard() {
    state.board = [0, 0, 0, 0, 0, 0, 0, 0, 0];
    state.turn = PLAYER;
    state.disabled = false;

    for (const child of document.getElementById("board").children)
        child.classList.remove("x", "o", "winnerCell", "disabled");

    document.getElementById("turn").textContent = "Next move: X";
}
