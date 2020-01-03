from data.reader import read_boxes_from_file
from solution.solver import pack_boxes
from modes.modes import solve_from_input, generate_and_solve
import argparse

def main():
    parser = argparse.ArgumentParser(description='Boxes algorithm - AAL Project, author: Kacper Biegajski')
    parser.add_argument('-m1', type=str, help='Give an input file name')
    parser.add_argument('-m2', type=str, help='Give an output file name. Generates instation of problem and solves it (-n and -mr flags required)')
    parser.add_argument('-m3', action='store_true', help='Time measure for different problem instances (-n -k -step -r flags required)')
    parser.add_argument('-n', type=int, help='Size of problem instance')
    parser.add_argument('-mr', type=int, help='Max length of edge of the box')
    parser.add_argument('-k', type=int, help='Number of measured sizes of problem instances')
    parser.add_argument('-step', type=int, help='Increment step')
    parser.add_argument('-r', type=int, help='Number of tests for each size')

    args = parser.parse_args()

    if args.m1 is not None:
        solve_from_input(args.m1)
    elif args.m2 is not None:
        if args.n is None or args.mr is None:
            print('-n or -mr flag is missing')
        else:
            generate_and_solve(args.m2, args.n, args.mr)

if __name__ == '__main__':
    main()
    
