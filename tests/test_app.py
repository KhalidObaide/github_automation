import unittest
from app import db_uri

class TestApp(unittest.TestCase):
    def test_(self):
        # Create a simple account
        self.assertEqual(db_uri, "DB_URI")
