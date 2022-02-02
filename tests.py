from app import app
from flask import session
from unittest import TestCase
from boggle import Boggle 

class TestBoggleGame(TestCase):
    """
        Test  the functions from the boggle game project
    """

    def test_index_page(self):
        with app.test_client() as client:
            res = client.get('/')
            html= res.get_data(as_text=True)
            self.assertEqual(res.status_code,200)
            
            self.assertIn('<form class="form-inline" >',html)
            #self.assertIn(f'<td class="col-md-1">E</td>',html)

    def test_valid_word(self):
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['board'] =[
                        ['H','U','Z','V','P'],
                        ['X','G','N','W','P'],
                        ['D','Q','T	','W','U'],
                        ['S','Z','V','R','V'] ,
                        ['B','C','J','T','P']
                    ]
                self.assertEqual(Boggle.check_valid_word( session['board'], 'W'), 'ok')
                self.assertEqual(Boggle.check_valid_word( session['board'], '1'), 'not-word')
                self.assertEqual(Boggle.check_valid_word( session['board'], 'A'), 'not-on-board')
