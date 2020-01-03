from data.reader import read_boxes_from_file
from data.generator import generate_boxes
from solution.solver import pack_boxes

def solve_from_input(filename):
    boxes = read_boxes_from_file(filename)
    packed_boxes, total_volume = pack_boxes(boxes)

    with open(f'output_{filename}', 'w') as writer:
        for stack in packed_boxes:
            writer.write(f'{stack}\n-----------------------------------\n')
        
        writer.write(f'Total volume: {total_volume}')

def generate_and_solve(filename, count, max_range):
    boxes = generate_boxes(count, max_range)
    packed_boxes, total_volume = pack_boxes(boxes)

    with open(filename, 'w') as writer:
        for stack in packed_boxes:
            writer.write(f'{stack}\n-----------------------------------\n')
        
        writer.write(f'Total volume: {total_volume}')