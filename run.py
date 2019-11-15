import sys
from data.reader import read_boxes_from_file
from solution.solver import pack_boxes

if __name__ == '__main__':
    boxes = read_boxes_from_file(sys.argv[1])
    print(pack_boxes(boxes))
