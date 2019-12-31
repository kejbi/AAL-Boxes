from solution.utils import volume, rotate_box

def read_boxes_from_file(filename):
    boxes_list = []
    with open(filename, 'r') as reader:
        for line in reader:
            float_values = list(map(float, line.split(',')))
            float_values.append(volume(*float_values))
            box = rotate_box(float_values)
            boxes_list.append(box)
    
    return boxes_list