import unittest
from flask import Flask, jsonify
from app.counter import Counter

class CounterTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.counter = Counter()
        self.app.testing = True

    def test_increment(self):
        with self.app.test_client() as client:
            response = client.get('/api/increment')
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['value'], self.counter.increment())

    def test_decrement(self):
        with self.app.test_client() as client:
            response = client.get('/api/decrement')
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['value'], self.counter.decrement())

    def test_reset(self):
        with self.app.test_client() as client:
            response = client.get('/api/reset')
            data = response.get_json()
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['value'], self.counter.reset())

if __name__ == '__main__':
    unittest.main()