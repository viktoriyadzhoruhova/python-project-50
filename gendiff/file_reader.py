import json
import os
import yaml


def read_file(file_path):
    """Reads a file and returns its content as a dictionary."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    _, file_extension = os.path.splitext(file_path)
    if file_extension == '.json':
        return read_json(file_path)
    elif file_extension in ['.yml', '.yaml']:
        return read_yaml(file_path)
    else:
        raise ValueError(f"Unsupported file format: '{file_extension}'")


def read_json(file_path):
    """Reads a JSON file and returns its content as a dictionary."""
    with open(file_path, 'r') as file:
        return json.load(file)


def read_yaml(file_path):
    """Reads a YAML file and returns its content as a dictionary."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
