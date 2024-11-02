from gendiff.diff_generator import generate_diff


def test_generate_diff():
    file1 = 'file1.json'
    file2 = 'file2.json'

    expected_output = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    assert generate_diff(file1, file2) == expected_output
