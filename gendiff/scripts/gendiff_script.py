#!/usr/bin/env python3
from gendiff import generate_diff
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = parser.parse_args()
    return parser.parse_args()


def main():
    args = parse_args()
    generate_diff(args.first_file, args.second_file)
    

if __name__ == '__main__':
    main()
