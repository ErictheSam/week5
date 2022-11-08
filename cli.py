# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, legal_move, board_full, get_winner, other_player


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = "X"
    while winner == None:
        '''Showing the board to the user.'''
        print("Current player is {}".format(player))
        print(board[0][0], board[0][1], board[0][2])
        print(board[1][0], board[1][1], board[1][2])
        print(board[2][0], board[2][1], board[2][2])
        '''Inputing a move from the player.'''
        '''Updating the board.'''
        move_legal = False
        while(move_legal == False):
            row = int(input("Input the row ranging from 1 to 3: "))
            col = int(input("Input the column ranging from 1 to 3: "))
            if legal_move(board,row,col) == True:
                board[row-1][col-1] = player
                move_legal = True
            else:
                print("Move is illegal, please input the row and column again")
        
        winner = get_winner(board)
        if board_full(board) and winner == None:
            winner = "Draw"
        ''' Updating whose turn it is.'''
        player = other_player(player)
    print("Winner is: {}".format(winner))
