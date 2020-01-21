from data.reader import read_boxes_from_file
from data.generator import generate_boxes, generate_boxes_hard
from solution.solver import pack_boxes, pack_boxes_reverse, dynamic_pack_boxes
from time import time
from statistics import mean, median
from copy import deepcopy

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
        avg_time = mean(step_times)
        times.append(avg_time)
        number_of_boxes += step
    return times, median(times), median(range(start_count, number_of_boxes, step))

def generate_results(times, median_time, n, n_median, step):
    with open('time_test_results.txt', 'w') as writer:
        writer.write(f't(median) = {median_time}\nn --- t(n) --- q(n)\n=======================\n')
        for t in times:
            q = (t * (n_median ** 2)) / ((n ** 2) * median_time)
            writer.write(f'{n} --- {t} --- {q}\n')
            n += step

def compare():
    counter1 = 0
    counter2 = 0
    for i in range(0,1000):
        boxes = generate_boxes(20, 10)
        boxes2 = deepcopy(boxes)
        boxes3 = deepcopy(boxes)
        packed1, vol1 = pack_boxes(boxes)
        packed2, vol2 =  pack_boxes_reverse(boxes2)
        packed3, vol3 = dynamic_pack_boxes(boxes3)
        if vol2 <= vol1:
            print(vol1, vol2)
            counter1 += 1

        if vol3 <= vol1:
            print(vol1, vol3)
            counter2 += 1

    print(f'dynamic byl lepszy lub równy {counter2} razy z 1000')
    print(f'reverse byl lepszy lub równy {counter1} razy z 1000')

