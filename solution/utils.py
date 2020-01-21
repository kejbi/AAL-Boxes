def volume(x, y, z):
    return x*y*z

def sort_boxes(boxes_list, reverse):
    boxes_list.sort(key = lambda x : x[3], reverse = reverse)
    return boxes_list

def rotate_box(box):
    rotated_box = box[:3]
    rotated_box.sort(reverse=True)
    rotated_box.append(box[3])
    return tuple(rotated_box)