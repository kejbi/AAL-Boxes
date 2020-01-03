from data.reader import read_boxes_from_file
from data.generator import generate_boxes, generate_boxes_hard
from solution.solver import pack_boxes
from time import time
from statistics import mean, median

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

def time_test(start_count, step, k, r):
    number_of_boxes = start_count
    times = []
    for i in range(0, k):
        step_times = []
        for j in range(0, r):
            boxes = generate_boxes_hard(number_of_boxes, 10)
            start = time()
            pack_boxes(boxes)
            end = time()
            step_times.append(end-start)
        times.append(mean(step_times))
        number_of_boxes += step
    return times, median(times)

