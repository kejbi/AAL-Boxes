from .utils import sort_boxes
from .ford_fulkerson import FlowNetwork
from copy import deepcopy

def pack_boxes(boxes_list):
    sorted_boxes = sort_boxes(boxes_list, True)
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

def pack_boxes_reverse(boxes_list):
    sorted_boxes = sort_boxes(boxes_list, False)
    packed_boxes = []
    total_volume = 0
    while len(sorted_boxes) != 0:
        box = sorted_boxes[0]
        box_stack = [box]
        
        sorted_boxes.remove(box)
        i = 0
        while i < len(sorted_boxes):
            bigger_box = sorted_boxes[i]
            if bigger_box[0] > box[0] and bigger_box[1] > box[1] and bigger_box[2] > box[2]:
                box_stack.append(bigger_box)
                box = bigger_box
                sorted_boxes.remove(bigger_box)
            else:
                i+=1
        packed_boxes.append(box_stack)
        total_volume += box_stack[-1][3]

        
    return packed_boxes, total_volume

# def dynamic_pack_boxes(boxes):
#     sorted_boxes = sort_boxes(boxes, False)
#     table = [[sorted_boxes[0]]]
#     for box in sorted_boxes[1:]:
#         #sorting stacks by volume of each stack (biggest box volume)
#         sorted_stacks = sorted(table, key = lambda x : x[-1][3]) #[-1][3] means volume of stack (volume of biggest box in stack)
#         added = False
#         for stack in sorted_stacks:
#             if box[0] > stack[-1][0] and box[1] > stack[-1][1] and box[2] > stack[-1][2]:
#                 stack.append(box)
#                 added = True
#                 break
#         if added == False: sorted_stacks.append([box])
#         table = sorted_stacks

#     total_volume = 0
#     for volume in table:
#         total_volume += volume[-1][3]

#     return table, total_volume

def flow_pack_boxes(boxes):
    graph = FlowNetwork()
    graph.AddVertex('start')
    graph.AddVertex('target')
    sorted_boxes = sort_boxes(boxes, True)

    for box in sorted_boxes:
        graph.AddVertex(('u', box))
        graph.AddVertex(('v', box))
        graph.AddEdge('start',('u', box),1)
        graph.AddEdge(('v', box), 'target', 1)

    for box in sorted_boxes:
        for box2 in boxes:
            if box[0] < box2[0] and box[1] < box2[1] and box[2] < box2[2]:
                graph.AddEdge(('u', box), ('v', box2), 1)

    return graph.MaxFlow('start', 'target')