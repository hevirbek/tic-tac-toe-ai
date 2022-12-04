
// game board
var board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
];

player = 1;
pc = 2;

// make a move
function makeMove(board, player, row, col) {
    if (board[row][col] === 0) {
        board[row][col] = player;
        return true;
    }
    return false;
}

// is winner
function isWinner(board, player) {
    // check rows
    for (var i = 0; i < 3; i++) {
        if (board[i][0] === player && board[i][1] === player && board[i][2] === player) {
            return true;
        }
    }
    // check cols
    for (var i = 0; i < 3; i++) {
        if (board[0][i] === player && board[1][i] === player && board[2][i] === player) {
            return true;
        }
    }
    // check diagonals
    if (board[0][0] === player && board[1][1] === player && board[2][2] === player) {
        return true;
    }
    if (board[2][0] === player && board[1][1] === player && board[0][2] === player) {
        return true;
    }

    return false;
}

// is space free
function isSpaceFree(board, row, col) {
    return board[row][col] === 0;
}

// is board full
function isBoardFull(board) {
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            if (board[i][j] === 0) {
                return false;
            }
        }
    }
    return true;
}

// minimax algorithm
function minimax(board, depth, isMaximizing) {
    if (isWinner(board, pc)) {
        return 1;
    }
    if (isWinner(board, player)) {
        return -1;
    }
    if (isBoardFull(board)) {
        return 0;
    }
    if (isMaximizing) {
        var bestScore = -Infinity;
        for (var i = 0; i < 3; i++) {
            for (var j = 0; j < 3; j++) {
                if (isSpaceFree(board, i, j)) {
                    board[i][j] = pc;
                    var score = minimax(board, depth + 1, false);
                    board[i][j] = 0;
                    bestScore = Math.max(score, bestScore);
                }
            }
        }
        return bestScore;
    } else {
        var bestScore = Infinity;
        for (var i = 0; i < 3; i++) {
            for (var j = 0; j < 3; j++) {
                if (isSpaceFree(board, i, j)) {
                    board[i][j] = player;
                    var score = minimax(board, depth + 1, true);
                    board[i][j] = 0;
                    bestScore = Math.min(score, bestScore);
                }
            }
        }
        return bestScore;
    }
}

// find best move
function findBestMove(board) {
    var bestScore = -Infinity;
    var move = {};
    for (var i = 0; i < 3; i++) {
        for (var j = 0; j < 3; j++) {
            if (isSpaceFree(board, i, j)) {
                board[i][j] = pc;
                var score = minimax(board, 0, false);
                board[i][j] = 0;
                if (score > bestScore) {
                    bestScore = score;
                    move = { i, j };
                }
            }
        }
    }
    return move;
}


box1 = document.getElementById("box0");
box2 = document.getElementById("box1");
box3 = document.getElementById("box2");
box4 = document.getElementById("box3");
box5 = document.getElementById("box4");
box6 = document.getElementById("box5");
box7 = document.getElementById("box6");
box8 = document.getElementById("box7");
box9 = document.getElementById("box8");

boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9];

result = document.getElementById("result");

disableBoxes = () => {
    boxes.forEach((box) => {
        box.disabled = true;
    });
};

enableBoxes = () => {
    boxes.forEach((box) => {
        box.disabled = false;
    });
};

boxes.forEach(box => {
    box.addEventListener('click', function () {
        if (box.innerHTML === "") {
            // player move
            box.innerHTML = "X";
            makeMove(board, player, Math.floor(box.id[3] / 3), box.id[3] % 3);
            if (isWinner(board, player)) {
                result.innerHTML = "Kazandın!";
                disableBoxes();
                return
            }
            if (isBoardFull(board)) {
                result.innerHTML = "Berabere!";
                disableBoxes();
                return
            }

            // pc move
            var move = findBestMove(board);
            makeMove(board, pc, move.i, move.j);
            boxes[move.i * 3 + move.j].innerHTML = "O";
            if (isWinner(board, pc)) {
                result.innerHTML = "Kaybettin!";
                disableBoxes();
                return
            }
            if (isBoardFull(board)) {
                result.innerHTML = "Berabere!";
                disableBoxes();
                return
            }
        }
    });
});


// reset board
function resetBoard() {
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ];
    boxes.forEach(box => {
        box.innerHTML = "";
    });
    result.innerHTML = "";
    enableBoxes();
}


restartBtn = document.getElementById("restart");
restartBtn.addEventListener('click', function () {
    resetBoard();
}
);