from .utils import sort_boxes

def pack_boxes(boxes_list):
    sorted_boxes = sort_boxes(boxes_list)
    packed_boxes = []
    total_volume = 0
        
    while len(sorted_boxes) != 0:
        box = sorted_boxes[0]
        box_stack = [box]
        total_volume += box[3]
        sorted_boxes.remove(box)
        i = 0
        while i < len(sorted_boxes):
            smaller_box = sorted_boxes[i]
            if smaller_box[0] < box[0] and smaller_box[1] < box[1] and smaller_box[2] < box[2]:
                box_stack.append(smaller_box)
                box = smaller_box
                sorted_boxes.remove(smaller_box)
            else:
                i+=1
        packed_boxes.append(box_stack)

        
    return packed_boxes, total_volume