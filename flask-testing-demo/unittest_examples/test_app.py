from app import app
from unittest import TestCase

class ColorViewsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        print("inside setup class")

    @classmethod
    def tearDownClass(cls):
        print("outside once per class")
        
    def setUp(self):
        print("RUNS BEFORE EVERTY TEST")

    def tearDown(self):
        print('RUNS AFTER EVERY TEST')

    def test_color_form(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1> Color form </h1>', html)

    def test_color_submit(self):
        with app.test_client() as client:
            res = client.post('/fav-color', data={'color': 'orange'})

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h3> Woah! I like orange, too </h3>', html)

    def test_redirection(self):
        with app.test_client() as client:
            res = client.get('/redirect-me')

            self.assertEqual(res.status_code, 302)
            self.asserEqual(res.location, 'http://localhost/') 

    def test_redirection_followed(self):
        with app.test_client as client:
            res = client.get('/redirect-me', follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 302)
            self.assertIn('<h1> Color form </h1>', html)

    def test_session_count(self):
        with app.test_client as client:
            res = client.get('/')

            self.assertEqual(res.status_code, '200')
            self.assertEqual(session['count'], 1)