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
        
        
if __name__ =='__main__':
    unittest.main()
