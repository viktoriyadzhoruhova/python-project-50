import argparse
import json

def load_json(file_path):
    """Load JSON file and return its content."""
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='First configuration file')
    parser.add_argument('second_file', type=str, help='Second configuration file')
    parser.add_argument('-f', '--format', help='set format of output', default='plain')

    args = parser.parse_args()

    # Load JSON files
    first_data = load_json(args.first_file)
    second_data = load_json(args.second_file)

    print(f"Comparing {args.first_file} and {args.second_file} with {args.format} format.")
    print("First file data:", first_data)
    print("Second file data:", second_data)

if __name__ == '__main__':
    main()
