from gendiff.file_reader import read_file
from gendiff.formatters.stylish import format_stylish


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    diff = build_diff_tree(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)

    raise ValueError(f"Unsupported format: {format_name}")


def build_diff_tree(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        if key not in data2:
            diff.append({'key': key, 'status': 'removed', 'value': data1[key]})
        elif key not in data1:
            diff.append({'key': key, 'status': 'added', 'value': data2[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            children = build_diff_tree(data1[key], data2[key])
            diff.append({'key': key, 'status': 'nested', 'children': children})
        elif data1[key] != data2[key]:
            diff.append({
                'key': key,
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })
        else:
            diff.append({
                'key': key,
                'status': 'unchanged',
                'value': data1[key]
            })

    return diff
