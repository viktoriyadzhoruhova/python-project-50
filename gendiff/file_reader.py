import os
import json
import yaml


def read_file(file_path):
    """Reads the file content and returns it as a string."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    with open(file_path, 'r') as file:
        return file.read()


def parse_json(data):
    """Parses JSON data from a string."""
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON data: {e}")


def parse_yaml(data):
    """Parses YAML data from a string."""
    try:
        return yaml.safe_load(data)
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML data: {e}")


def parse_data(data, file_extension):
    """Parses data from a string based on its format."""
    if file_extension == '.json':
        return parse_json(data)
    elif file_extension in ['.yml', '.yaml']:
        return parse_yaml(data)
    else:
        raise ValueError(f"Unsupported file format: '{file_extension}'")


def load_data(file_path):
    """Reads and parses data from a file."""
    data = read_file(file_path)
    _, file_extension = os.path.splitext(file_path)
    return parse_data(data, file_extension)
