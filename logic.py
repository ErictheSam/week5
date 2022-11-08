# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    """Makes up an empty board."""
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def legal_move(board, row, col):
    """Determines if a move at (row,col) is legal.
    Returns True if the move is legal (previous place is None)."""
    return 1 <= row < 4 and 1 <= col < 4 and board[row-1][col-1] == None

def board_full(board):
    """Determines if the given board is full.
    Returns True of False."""
    for i in range(3):
        for j in range(3):
            if(board[i][j] == None):
                return False
    return True

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    winner = None
    for i in range(3): # scan to find if there is a legal winner in row/col
        if(board[i][0] != None and board[i][0] == board[i][1] and board[i][0] == board[i][2]):
            winner = board[i][0]
            return winner
        elif(board[0][i] != None and board[0][i] == board[1][i] and board[0][i] == board[2][i]):
            winner = board[0][i]
            return winner
    '''scan to find if there is a legal winner in diagonals'''
    if(board[0][0] != None and board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        winner = board[0][0]
    elif(board[2][0] != None and board[2][0] == board[1][1] and board[0][2] == board[1][1]):
        winner = board[2][0]
    return winner


def other_player(player):
    """Given the character for a player, returns the other player."""
    assert player == "O" or player == "X", "Not the proper player!"
    if(player == "X"):
        return "O"
    else:
        return "X"
