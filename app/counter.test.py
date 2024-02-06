import unittest
from app.counter import Counter

class CounterTestCase(unittest.TestCase):
    def test_increment(self):
        counter = Counter()
        self.assertEqual(counter.increment(), 1)

    def test_decrement(self):
        counter = Counter()
        self.assertEqual(counter.decrement(), 0)

    def test_reset(self):
        counter = Counter()
        counter.increment()
        self.assertEqual(counter.reset(), 0)

    def test_increment_multiple_times(self):
        counter = Counter()
        for i in range(5):
            counter.increment()
        self.assertEqual(counter.value, 5)

    def test_decrement_multiple_times(self):
        counter = Counter()
        counter.increment()
        for i in range(3):
            counter.decrement()
        self.assertEqual(counter.value, 0)

    def test_increment_and_reset(self):
        counter = Counter()
        counter.increment()
        self.assertEqual(counter.reset(), 0)

    def test_decrement_below_zero(self):
        counter = Counter()
        self.assertEqual(counter.decrement(), 0)

if __name__ == '__main__':
    unittest.main()