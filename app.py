from flask import Flask, request, render_template, redirect, flash, jsonify, session, make_response
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle


app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# Initialize the Boggle game
boggle_game = Boggle()

@app.route('/game')
def start_game():
    """Generate the 5x5 board of letters, store it into the session under the key "board", and display the board on the page
    as a table with a form to submit words the user sees on the board."""
    session["board"] = boggle_game.make_board()
    return render_template("game.html")

