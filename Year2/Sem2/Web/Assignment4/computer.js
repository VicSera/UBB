const MAX_DEPTH = 10;

// MINMAX algorithm
// Computer tries to maximize score
// Player tries to minimize score
function getBestMove(board, isComputer = true, stepsRemaining = MAX_DEPTH) {
    if (stepsRemaining === 0 || evaluateState(board).score !== 0 || !movesRemaining(board))
        return {
            score: evaluateState(board).score,
            move: 0,
            distance: MAX_DEPTH - stepsRemaining
        };

    let bestEvaluation = isComputer? -2 : 2;
    let bestMove = -1;
    let bestDistance = -1;
    for (let index = 0; index < board.length; index++) {
        if (board[index] === 0) {
            let simulatedBoard = [...board];
            simulatedBoard[index] = isComputer? COMPUTER : PLAYER;
            const childMove = getBestMove(simulatedBoard, !isComputer, stepsRemaining - 1);

            if (isComputer) {
                if (childMove.score > bestEvaluation ||
                    (childMove.score === bestEvaluation && childMove.distance < bestDistance)) {
                    bestEvaluation = childMove.score;
                    bestMove = index;
                    bestDistance = childMove.distance;
                }
            }
            else {
                if (childMove.score < bestEvaluation ||
                    (childMove.score === bestEvaluation && childMove.distance < bestDistance)) {
                    bestEvaluation = childMove.score;
                    bestMove = index;
                    bestDistance = childMove.distance;
                }
            }
        }
    }

    return {
        score: bestEvaluation,
        move: bestMove,
        distance: MAX_DEPTH - stepsRemaining + 1
    };
}

function evaluateState(board) {
    for (let row = 0; row < 3; row++)
        if (board[3 * row] !== 0 && board[3 * row] === board[3 * row + 1] && board[3 * row + 1] === board[3 * row + 2])
            return {
                winner: board[3 * row],
                score: COMPUTER === board[3 * row]? 1 : -1,
                winnerSquares: [3 * row, 3 * row + 1, 3 * row + 2]
            }
    for (let col = 0; col < 3; col++)
        if (board[col] !== 0 && board[col] === board[col + 3] && board[col + 3] === board[col + 6])
            return {
                winner: board[col],
                score: COMPUTER === board[col]? 1 : -1,
                winnerSquares: [col, col + 3, col + 6]
            };
    if (board[0] !== 0 && board[0] === board[4] && board[4] === board[8])
        return {
            winner: board[0],
            score: COMPUTER === board[0]? 1 : -1,
            winnerSquares: [0, 4, 8]
        }
    if (board[2] !== 0 && board[2] === board[4] && board[4] === board[6])
        return {
            winner: board[2],
            score: COMPUTER === board[2]? 1 : -1,
            winnerSquares: [2, 4, 6]
        }
    return {
        winner: 0,
        score: 0,
        winnerSquares: []
    };
}

function movesRemaining(board) {
    for (let cell of board)
        if (cell === 0)
            return true;
    return false;
}
