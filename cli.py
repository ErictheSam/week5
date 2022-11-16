# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import FullBoard


if __name__ == '__main__':
    winner = None
    '''Input the mode'''
    mode = input("Select mode, 1 for single player, 2 for double player")
    if(mode == "1"):
        single = True
    else:
        single = False
    board = FullBoard(single)
    while winner == None:
        '''Showing the board to the user.'''
        board.print_board()
        '''Inputing a move from the player.'''
        '''Updating the board.'''
        if(mode == "1" and board.get_player() == "O"):
            row, col = board.random_chess()
            board.move(row,col)
        else:
            move_legal = False
            while(move_legal == False):
                row = int(input("Input the row ranging from 1 to 3: "))
                col = int(input("Input the column ranging from 1 to 3: "))
                if board.legal_move(row,col) == True:
                    board.move(row,col)
                    move_legal = True
                else:
                    print("Move is illegal, please input the row and column again")
        
        winner = board.get_winner()
        if board.board_full() and winner == None:
            winner = "Draw"
        ''' Updating whose turn it is.'''
        board.flip_player()
    print("Winner is: {}".format(winner))
