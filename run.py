import argparse
import os
from kdpv_generator import KDPVGenerator


def generate(filename):
    generator = KDPVGenerator.from_yml(filename)
    generator.generate()


def main():
    parser = argparse.ArgumentParser(description='KDPV Generator')
    parser.add_argument('filename', nargs='?', default='data.yml', help='data file (default: data.yml)')
    args = parser.parse_args()
    if not args.filename:
        parser.print_help()
    else:
        if not os.path.isfile(args.filename):
            exit('Unable to open file: {}'.format(args.filename))
        generate(args.filename)


if __name__ == '__main__':
    main()
