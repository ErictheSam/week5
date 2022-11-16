# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import random

class FullBoard:

    def __init__(self, single):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.single = single
        self.player = "X"
    
    def print_board(self):
        """Print the board up."""
        print("Current player is {}".format(self.player))
        print(self.board[0][0], self.board[0][1], self.board[0][2])
        print(self.board[1][0], self.board[1][1], self.board[1][2])
        print(self.board[2][0], self.board[2][1], self.board[2][2])

    def legal_move(self, row, col):
        """Determines if a move at (row,col) is legal.
        Returns True if the move is legal (previous place is None)."""
        return 1 <= row < 4 and 1 <= col < 4 and self.board[row-1][col-1] == None

    def move(self, row, col):
        assert self.legal_move(row, col) == True
        self.board[row-1][col-1] = self.player

    def board_full(self):
        """Determines if the given board is full.
        Returns True of False."""
        for i in range(3):
            for j in range(3):
                if(self.board[i][j] == None):
                    return False
        return True

    def get_winner(self):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        winner = None
        for i in range(3): # scan to find if there is a legal winner in row/col
            if(self.board[i][0] != None and self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2]):
                winner = self.board[i][0]
                return winner
            elif(self.board[0][i] != None and self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i]):
                winner = self.board[0][i]
                return winner
        '''scan to find if there is a legal winner in diagonals'''
        if(self.board[0][0] != None and self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]):
            winner = self.board[0][0]
        elif(self.board[2][0] != None and self.board[2][0] == self.board[1][1] and self.board[0][2] == self.board[1][1]):
            winner = self.board[2][0]
        return winner

    def random_chess(self):
        """Sets up a random chessboard for further """
        idle_list = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == None:
                    idle_list.append((i+1,j+1))
        num = random.randint(0,len(idle_list)-1)
        return idle_list[num]

    def flip_player(self):
        """Given the character for a player, returns the other player."""
        if(self.player == "X"):
            self.player = "O"
        else:
            self.player = "X"
    
    def get_player(self):
        """Get the player of the game."""
        return self.player
