import argparse
from gendiff.diff_generator import generate_diff as generate_diff_data


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        'first_file',
        type=str,
        help='First configuration file'
    )
    parser.add_argument(
        'second_file',
        type=str,
        help='Second configuration file'
    )
    parser.add_argument(
        '-f', '--format',
        help='Set format of output',
        choices=['stylish', 'plain', 'json'],
        default='stylish'
    )

    args = parser.parse_args()

    diff = generate_diff_data(args.first_file, args.second_file)
    if diff:
        print(diff)


if __name__ == '__main__':
    main()
