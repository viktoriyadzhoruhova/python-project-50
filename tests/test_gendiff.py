from gendiff.diff_generator import generate_diff


def test_generate_diff_json():
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

    generated_output = generate_diff(file1, file2)
    print("Generated Output JSON:\n", generated_output)
    assert generated_output == expected_output


def test_generate_diff_yaml():
    file1 = 'file1.yml'
    file2 = 'file2.yml'

    expected_output = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    generated_output = generate_diff(file1, file2)
    print("Generated Output YAML:\n", generated_output)
    assert generated_output == expected_output
