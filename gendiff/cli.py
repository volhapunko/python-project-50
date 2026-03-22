import argparse

from gendiff import generate_diff
from gendiff.file_reader import read_file


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output (stylish, plain, json)')

    args = parser.parse_args()

    data1 = read_file(args.first_file)
    data2 = read_file(args.second_file)

    diff = generate_diff(data1, data2, args.format)
    print(diff)