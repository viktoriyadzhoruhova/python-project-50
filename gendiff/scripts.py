import argparse
from gendiff.file_reader import read_file
from gendiff.diff_generator import generate_diff


def generate_diff(file_path1, file_path2):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    diff = {
        key: (data1.get(key), data2.get(key))
        for key in set(data1) | set(data2)
    }

    for key, (value1, value2) in diff.items():
        if value1 != value2:
            if value1 is None:
                print(f"  + {key}: {value2}")
            elif value2 is None:
                print(f"  - {key}: {value1}")
            else:
                print(f"  - {key}: {value1}")
                print(f"  + {key}: {value2}")
        else:
            print(f"    {key}: {value1}")

def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str, help='First configuration file')
    parser.add_argument('second_file', type=str, help='Second configuration file')
    parser.add_argument('-f', '--format', help='Set format of output', choices=['stylish', 'plain', 'json'], default='stylish')

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

if __name__ == '__main__':
    main()
