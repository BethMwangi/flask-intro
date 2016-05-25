from app import app
import unittest


class FlaskTextCase(unittest.TestCase):
    def text_index(self):
        tester= app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
if __name__ =='__main__':
    unittest.main()
