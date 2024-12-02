import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from app import app

class TestBookRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    
    def test_new_book_route(self):
        response = self.app.get("/book_form")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<form', response.data)
    
