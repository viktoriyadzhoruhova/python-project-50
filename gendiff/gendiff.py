from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.json_formatter import format_json
from gendiff.diff_generator import generate_diff
from gendiff.cli import get_args


FORMATTERS = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json
}


def main():
    args = get_args()

    file_path1 = args.first_file
    file_path2 = args.second_file
    formatter = args.format

    diff = generate_diff(file_path1, file_path2, formatter)
    print(diff)


if __name__ == '__main__':
    main()
