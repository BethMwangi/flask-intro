from app import app
import unittest


class FlaskTextCase(unittest.TestCase):
    #to check whether flask was set up correctly
    def test_index(self):
        tester= app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    #ensure login page was set up correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue('Please login' in response.data)
    
    #ensure login page behaves correctly when given correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login', 
            data=dict(username="admin", password="admin"), 
            follow_redirects=True
        )
        self.assertIn('You were just logged in!', response.data)
  

    #ensure logout behaves correctly 
        
if __name__ =='__main__':
    unittest.main()
