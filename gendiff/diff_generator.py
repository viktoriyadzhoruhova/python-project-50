from gendiff.find_diff import find_diff
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.json_formatter import format_json
from gendiff.file_reader import load_data

FORMATTERS = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json
}


def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)

    diff = find_diff(data1, data2)

    return FORMATTERS[formatter](diff)
