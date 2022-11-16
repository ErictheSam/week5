import unittest
from logic import FullBoard


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = FullBoard(True)
        board.board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(board.get_winner(), 'X')
        board.board = [
            ['X', 'O', 'O'],
            [None, 'O', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(board.get_winner(), 'O')
        board.board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
            ['X', 'X', 'O'],
        ]
        self.assertEqual(board.get_winner(), None)

    def test_legal_move(self):
        board = FullBoard(True)
        board.board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        row = 4
        column = 2
        self.assertEqual(board.legal_move(row,column), False)
        row = 2
        column = 2
        self.assertEqual(board.legal_move(row,column), False)
        row = 2
        column = 1
        self.assertEqual(board.legal_move(row,column), True)

    def test_board_full(self):
        board = FullBoard(True)
        board.board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(board.board_full(), False)
        board.board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
            ['X', 'X', 'X'],
        ]
        self.assertEqual(board.board_full(), True)

    def test_flip(self):
        board = FullBoard(True)
        board.flip_player()
        self.assertEqual(board.player, "O")
        board.flip_player()
        self.assertEqual(board.player, "X")

    def test_random_chess(self):
        board = FullBoard(True)
        board.board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        row, col = board.random_chess()
        self.assertEqual(board.board[row-1][col-1], None)

    def test_move(self):
        board = FullBoard(True)
        board.move(1,1)
        self.assertEqual(board.board[0][0], "X")

if __name__ == '__main__':
    unittest.main()
