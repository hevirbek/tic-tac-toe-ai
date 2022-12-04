
import random
import streamlit as st

buttons = []


def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def makeMove(board, letter, move):
    board[move] = letter
    # change the button text
    if move in st.session_state:
        btn = st.button(letter, key=move)


def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            # down the right side
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def isSpaceFree(board, move):
    return board[move] == ' '


def getComputerMove(board, computerLetter, playerLetter):
    # use minimax algorithm to find the best move
    def minimax(board, depth, isMaximizing):
        if isWinner(board, computerLetter):
            return 1
        elif isWinner(board, playerLetter):
            return -1
        elif isBoardFull(board):
            return 0

        if isMaximizing:
            bestScore = -float('inf')
            for i in range(1, 10):
                if isSpaceFree(board, i):
                    board[i] = computerLetter
                    score = minimax(board, depth + 1, False)
                    board[i] = ' '
                    bestScore = max(score, bestScore)
            return bestScore
        else:
            bestScore = float('inf')
            for i in range(1, 10):
                if isSpaceFree(board, i):
                    board[i] = playerLetter
                    score = minimax(board, depth + 1, True)
                    board[i] = ' '
                    bestScore = min(score, bestScore)
            return bestScore

    bestScore = -float('inf')
    bestMove = None
    for i in range(1, 10):
        if isSpaceFree(board, i):
            board[i] = computerLetter
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = i
    return bestMove


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


st.title('Tic Tac Toe')
st.write('Welcome to Tic Tac Toe!')

# Reset the board
theBoard = [' '] * 10
# add 2 radio for choosing the letter
playerLetter, computerLetter = st.columns(2)
with playerLetter:
    letter = st.radio('Do you want to be X or O?', ('X', 'O'))
with computerLetter:
    if letter == 'X':
        computerLetter = 'O'
    else:
        computerLetter = 'X'

turn = whoGoesFirst()
st.write('The ' + turn + ' will go first.')

for i in range(1, 10):
    buttons.append(st.button(
        theBoard[i], key=i, on_click=lambda i=i: makeMove(theBoard, letter, i)))
