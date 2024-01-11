from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleTests(TestCase):
    """Test cases/methods for the Flask portion of the Boggle game, namely app.py."""
    def test_game(self):
        """Tests the route /game, making sure that the HTML template returned contains the Boggle board and the form to 
        submit words. Also checks to make sure the Flask session "board" key is a 5x5 board of uppercase alphabetical letters."""
        with app.test_client() as client:
            resp = client.get('/game')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<th colspan="5">Boggle Board</th>', html)
            self.assertIn('<label for="guess">Enter words you see on the board here: </label>', html)
            self.assertEqual(len(session["board"]), 5)
            self.assertEqual(len(session["board"][0]), 5)
            self.assertTrue(session["board"][0][0].isalpha())
            self.assertTrue(session["board"][0][0].isupper())

