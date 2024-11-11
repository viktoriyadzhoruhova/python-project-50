import argparse
from gendiff.diff_generator import generate_diff


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
    parser.add_argument(
        '-o', '--output',
        help='Output to a file instead of stdout',
        type=str
    )

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, format_name=args.format)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as output_file:
            output_file.write(diff + '\n')
    else:
        print(diff)


if __name__ == '__main__':
    main()
