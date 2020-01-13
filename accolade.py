#!/usr/bin/env python3
import argparse
from argparse import RawTextHelpFormatter
import sys
import re


def solution(data):
    sys.stdout.write('Executing, please wait...\n\n')
    minimum_n = 1
    maximum_n = 100000
    for n in range(minimum_n, maximum_n):
        try:
            data.index(n)
            continue
        except ValueError:
            sys.stdout.write('Smallest possible integer is %s\n' % n)
            return
    sys.stdout.write('Maximum value reached, could not find number in acceptable range %s\n' % maximum_n)


def numbers(input_value):
    output = re.sub(r'[\[\]\'\" ]', '', input_value)
    return [int(x) for x in output.split(',')]


def range_value(input_value):
    return re.sub(r'[\[\]\'\",. ]', '', input_value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='''
Task:
Write a function: solution(A), that, given an array A of N integers, returns the smallest positive integer 
(greater than 0) that does not occur in A
Examples:
-	For example, given A = [1,3,6,4,1,2], the function should return 5
- 	Given A = [1,2,3], the function should return 4
-	Given A = [-1,-3], the function should return 1
Input ranges:
Write an efficient algorithm for the following assumptions:
-	N is an integer within the range [1..100,000]
-	Each element of array A is an integer within the range [a1,000,000..1,000,000]
''',
        epilog='''
Author: Oleg Yapparov <oyapparov@gmail.com>
''',
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument('-v', '--value', type=numbers,
                        help='''Input values separated by comma without spaces, e.g. 1,3,6,4,1,2. Values can be 
                        negative''')
    parser.add_argument('-r', '--range', nargs=2, action='store', type=range_value,
                        help='''Input range of values, e.g. 1 10. This will become range(1, 10). Values can be 
                        negative''')
    args = parser.parse_args()

    if args.value is not None:
        value = [int(x) for x in args.value]
        solution(value)
        sys.exit(0)

    if args.range is not None:
        start = int(args.range[0])
        end = int(args.range[1])
        value = range(start, end)
        solution(value)
        sys.exit(0)

    parser.print_help(sys.stderr)
    sys.exit(1)
