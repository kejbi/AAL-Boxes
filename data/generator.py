from solution.utils import volume, rotate_box
import random

def generate_boxes(count, max_range):
    boxes = []
    for i in range(0, count):
        x = random.randint(1, max_range)
        y = random.randint(1, max_range)
        z = random.randint(1, max_range)
        box = [x, y, z, volume(x, y, z)]
        boxes.append(rotate_box(box))
    return boxes

def generate_boxes_hard(count, max_range):
    boxes = []
    for i in range(0, count):
        x = random.randint(1, max_range)
        y = random.randint(1, max_range)
        z = 0.987
        box = [x, y, z, volume(x, y, z)]
        boxes.append(rotate_box(box))
    return boxes
