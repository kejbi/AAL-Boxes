import unittest
from solution.solver import pack_boxes, pack_boxes_reverse, flow_pack_boxes

class TestSolver(unittest.TestCase):
    def test_pack_boxes(self):
        boxes = [(4.0, 3.0, 2.0, 24.0), (5.0, 2.0, 2.0, 20.0), (3.0, 2.0, 1.0, 6.0), (1.0, 1.0, 0.5, 0.5), (4.0, 1.0, 1.0, 4.0), (5.0, 3.0, 1.0, 15.0)]
        packed = [[(4.0, 3.0, 2.0, 24.0), (3.0, 2.0, 1.0, 6.0), (1.0, 1.0, 0.5, 0.5)], [(5.0, 2.0, 2.0, 20.0), (4.0, 1.0, 1.0, 4.0)], [(5.0, 3.0, 1.0, 15.0)]]
        solved_boxes, volume = pack_boxes(boxes)
        self.assertListEqual(solved_boxes, packed)
        self.assertEqual(volume, 59)

    def test_pack_boxes_reverse(self):
        boxes = [(4.0, 3.0, 2.0, 24.0), (5.0, 2.0, 2.0, 20.0), (3.0, 2.0, 1.0, 6.0), (1.0, 1.0, 0.5, 0.5), (4.0, 1.0, 1.0, 4.0), (5.0, 3.0, 1.0, 15.0)]
        packed = [[(1.0, 1.0, 0.5, 0.5), (3.0, 2.0, 1.0, 6.0), (4.0, 3.0, 2.0, 24.0)], [(4.0, 1.0, 1.0, 4.0), (5.0, 2.0, 2.0, 20.0)], [(5.0, 3.0, 1.0, 15.0)]]
        solved_boxes, volume = pack_boxes_reverse(boxes)
        self.assertListEqual(solved_boxes, packed)
        self.assertEqual(volume, 59)

    def test_pack_boxes_flow(self):
        boxes = [(4.0, 3.0, 2.0, 24.0), (5.0, 2.0, 2.0, 20.0), (3.0, 2.0, 1.0, 6.0), (1.0, 1.0, 0.5, 0.5), (4.0, 1.0, 1.0, 4.0), (5.0, 3.0, 1.0, 15.0)]
        packed = [[(4.0, 3.0, 2.0, 24.0), (3.0, 2.0, 1.0, 6.0)], [(5.0, 2.0, 2.0, 20.0), (4.0, 1.0, 1.0, 4.0)], [(5.0, 3.0, 1.0, 15.0), (1.0, 1.0, 0.5, 0.5)]]
        solved_boxes, volume = flow_pack_boxes(boxes)
        print(solved_boxes)
        self.assertListEqual(solved_boxes, packed)
        self.assertEqual(volume, 59)



if __name__ == '__main__':
    unittest.main()