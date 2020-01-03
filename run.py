from data.reader import read_boxes_from_file
from solution.solver import pack_boxes
import argparse

def main():
    parser = argparse.ArgumentParser(description='Boxes algorithm - AAL Project, author: Kacper Biegajski')
    parser.add_argument('-m1', type=str, help='Give a input file name')
    parser.add_argument('-m2', action='store_true', help='Generates instation of problem and solves it (-n and -mr flags required)')
    parser.add_argument('-m3', action='store_true', help='Time measure for different problem instances (-n -k -step -r flags required)')
    parser.add_argument('-n', type=int, help='Size of problem instance')
    parser.add_argument('-mr', type=int, help='Max length of edge of the box')
    parser.add_argument('-k', type=int, help='Number of measured sizes of problem instances')
    parser.add_argument('-step', type=int, help='Increment step')
    parser.add_argument('-r', type=int, help='Number of tests for each size')

    args = parser.parse_args()


if __name__ == '__main__':

    
