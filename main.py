
import random


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def makeMove(board, letter, move):
    board[move] = letter


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


def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def main():
    print('Welcome to Tic Tac Toe!')

    while True:
        # Reset the board
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                # Player's turn.
                printBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    printBoard(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        printBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'

            else:
                # Computer's turn.
                move = getComputerMove(theBoard, computerLetter, playerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    printBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        printBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'

        if not playAgain():
            break


if __name__ == '__main__':
    main()
