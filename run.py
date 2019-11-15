import sys
from data.reader import read_boxes_from_file

if __name__ == '__main__':
    boxes = read_boxes_from_file(sys.argv[1])
    print(boxes)
