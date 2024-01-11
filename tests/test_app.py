from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class BoggleTests(TestCase):
    """Test cases/methods for the Flask portion of the Boggle game, namely app.py."""

