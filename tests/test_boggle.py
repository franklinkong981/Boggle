from unittest import TestCase
from boggle import Boggle

class BoggleTestCase(TestCase):
    """Test methods/test cases for the Boggle class and its methods in boggle.py"""
    def testInit(self):
        """Test to see whether the Boggle object is properly initialized with the right attributes."""
        boggle_game = Boggle()
        self.assertIsInstance(boggle_game.words, list)
        self.assertIsInstance(boggle_game.words[0], str)

    def testMakeBoard(self):
        """Test to see whether the board returned from the makeBoard function in the Boggle class consists of the right dimensions and 
        contents"""
        boggle_game = Boggle()
        board = boggle_game.make_board()
        self.assertEqual(len(board), 5)
        self.assertEqual(len(board[0]), 5)
        self.assertTrue(board[0][0].isalpha())
        self.assertTrue(board[0][0].isupper())


