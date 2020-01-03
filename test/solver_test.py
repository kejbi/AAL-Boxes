import unittest
from solution.solver import pack_boxes

class TestSolver(unittest.TestCase):
    def test_pack_boxes(self):
        boxes = [(4.0, 3.0, 2.0, 24.0), (5.0, 2.0, 2.0, 20.0), (3.0, 2.0, 1.0, 6.0), (1.0, 1.0, 0.5, 0.5), (4.0, 1.0, 1.0, 4.0), (5.0, 3.0, 1.0, 15.0)]
        packed = [[(4.0, 3.0, 2.0, 24.0), (3.0, 2.0, 1.0, 6.0), (1.0, 1.0, 0.5, 0.5)], [(5.0, 2.0, 2.0, 20.0), (4.0, 1.0, 1.0, 4.0)], [(5.0, 3.0, 1.0, 15.0)]]
        solved_boxes, volume = pack_boxes(boxes)
        self.assertListEqual(solved_boxes, packed)
        self.assertEqual(volume, 59)

if __name__ == '__main__':
    unittest.main()