import pytest
from gendiff import generate_diff


@pytest.mark.parametrize("file1, file2, formatter, expected", [
    ("tests/fixtures/nested_file1.json",
     "tests/fixtures/nested_file2.json", 'plain',
     "tests/fixtures/expected_result_plain.txt"),
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'stylish',
     "tests/fixtures/expected_result_nested.txt"),
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json", 'json',
     "tests/fixtures/expected_result_nested.json"),
])
def test_generate_diff(file1, file2, formatter, expected):
    """
    Tests the generate_diff function with various input files and formats.

    Parameters:
    file1 (str): The path to the first input file.
    file2 (str): The path to the second input file.
    formatter (str): The format to use for generating the diff.
    expected (str): The path to the expected output file.
    """
    diff = generate_diff(file1, file2, formatter)
    expected_result = read_file(expected)
    assert diff == expected_result


def read_file(file_name):
    """
    Reads the contents of a file and returns it as a string.

    Parameters:
    file_name (str): The path to the file.

    Returns:
    str: The contents of the file as a string.
    """
    with open(file_name, 'r') as file:
        return file.read().strip()
