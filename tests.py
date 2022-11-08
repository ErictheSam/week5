import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        board = [
            ['X', 'O', 'O'],
            [None, 'O', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')
        board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
            ['X', 'X', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), None)

    def test_make_empty_board(self):
        board_new = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.make_empty_board(), board_new)

    def test_legal_move(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        row = 4
        column = 2
        self.assertEqual(logic.legal_move(board,row,column), False)
        row = 2
        column = 2
        self.assertEqual(logic.legal_move(board,row,column), False)
        row = 2
        column = 1
        self.assertEqual(logic.legal_move(board,row,column), True)

    def test_board_full(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.board_full(board), False)
        board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
            ['X', 'X', 'X'],
        ]
        self.assertEqual(logic.board_full(board), True)

    def test_other_player(self):
        player = "X"
        self.assertEqual(logic.other_player(player), "O")
        player = "O"
        self.assertEqual(logic.other_player(player), "X")
        player = "A"
        """This should be an assertion error."""
        with self.assertRaises(AssertionError):
            logic.other_player(player)


if __name__ == '__main__':
    unittest.main()
