import unittest
from app.routes import app

class TestApp(unittest.TestCase):
    
    def test_debug_mode(self):
        app.testing = True
        client = app.test_client()
        
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(app.debug)

    def test_home_route(self):
        app.testing = True
        client = app.test_client()
        
        response = client.get('/')
        self.assertEqual(response.data, b"Hello, World!")

if __name__ == '__main__':
    unittest.main()