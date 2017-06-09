# -*- coding: utf-8 -*-

import sys

from core import KDPVGenerator


def print_help():
    print('Usage: python run.py [data.yml]')


def generate(filename):
    generator = KDPVGenerator.from_yml(filename)
    generator.generate()


def main():
    if len(sys.argv) < 2:
        filename = 'data.yml'

    else:
        filename = sys.argv[1]

    if filename in {'help', '-h', '--help'}:
        print_help()

    else:
        generate(filename)


if __name__ == '__main__':
    main()
