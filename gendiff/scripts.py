import argparse
import json

def load_json(file_path):
    """Load JSON file and return its content."""
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_diff(first_data, second_data):
    """Generate difference between two JSON files."""
    diff = []
    
    all_keys = sorted(set(first_data.keys()) | set(second_data.keys()))  # Все ключи из обоих файлов, отсортированные

    for key in all_keys:
        if key in first_data and key in second_data:
            if first_data[key] == second_data[key]:
                diff.append(f"    {key}: {first_data[key]}")
            else:
                diff.append(f"  - {key}: {first_data[key]}")
                diff.append(f"  + {key}: {second_data[key]}")
        elif key in first_data:
            diff.append(f"  - {key}: {first_data[key]}")
        else:
            diff.append(f"  + {key}: {second_data[key]}")
    
    return "{\n" + "\n".join(diff) + "\n}"

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='First configuration file')
    parser.add_argument('second_file', type=str, help='Second configuration file')
    parser.add_argument('-f', '--format', help='set format of output', default='plain')

    args = parser.parse_args()

    # Load JSON files
    first_data = load_json(args.first_file)
    second_data = load_json(args.second_file)

    # Generate and print diff
    diff = generate_diff(first_data, second_data)
    print(diff)

if __name__ == '__main__':
    main()
