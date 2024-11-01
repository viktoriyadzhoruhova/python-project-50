import json
from gendiff.file_reader import read_file

def generate_diff(file_path1, file_path2):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        if key not in data2:
            diff.append(f"  - {key}: {format_value(data1[key])}")
        elif key not in data1:
            diff.append(f"  + {key}: {format_value(data2[key])}")
        elif data1[key] != data2[key]:
            diff.append(f"  - {key}: {format_value(data1[key])}")
            diff.append(f"  + {key}: {format_value(data2[key])}")
        else:
            diff.append(f"    {key}: {format_value(data1[key])}")

    return "{\n" + "\n".join(diff) + "\n}"

def format_value(value):
    """Форматирует значение для корректного вывода."""
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return value
    return str(value)
