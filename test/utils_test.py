import unittest
from solution.utils import volume, sort_boxes

class TestUtils(unittest.TestCase):

    def test_volume(self):
        self.assertEqual(volume(2, 3, 4), 24)

    def test_list_volume(self):
        box = [2, 3, 4]
        self.assertEqual(volume(*box), 24)

    def test_volume_float(self):
        self.assertEqual(volume(2.5, 3.4, 5.6), 2.5*3.4*5.6)

    def test_sort_boxes(self):
        boxes_list = [(1, 2, 3, 6), (2, 2, 3, 12), (1, 1, 1, 1)]
        sorted_boxes = [(2, 2, 3, 12), (1, 2, 3, 6), (1, 1, 1, 1)]
        self.assertListEqual(sort_boxes(boxes_list), sorted_boxes)

if __name__ == '__main__':
    unittest.main()