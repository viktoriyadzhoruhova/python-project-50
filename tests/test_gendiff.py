import json
from gendiff.diff_generator import generate_diff

def test_generate_diff():
    with open('tests/fixtures/file1.json') as f1, open('tests/fixtures/file2.json') as f2:
        first_data = json.load(f1)
        second_data = json.load(f2)
        
        expected_diff = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

        assert generate_diff(first_data, second_data) == expected_diff
