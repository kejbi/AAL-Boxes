import unittest
from data.reader import read_boxes_from_file

class TestUtils(unittest.TestCase):
    def test_read_boxes_from_file(self):
        read_boxes = [
            (3, 2, 2, 12),
            (6, 5, 2, 60),
            (3, 2, 1, 6),
            (1, 0.5, 0.1, 0.05),
            (1, 1, 1, 1),
            (4, 2, 1, 8)
        ]
        self.assertListEqual(read_boxes_from_file('test2.txt'), read_boxes)
    

if __name__ == '__main__':
    unittest.main()