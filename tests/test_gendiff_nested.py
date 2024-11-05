from gendiff.diff_generator import generate_diff


def test_generate_diff_nested():
    file1 = 'nested_file1.json'
    file2 = 'nested_file2.json'

    expected_output = ("{\n"
                       "        common: {\n"
                       "          + follow: false\n"
                       "            setting1: Value 1\n"
                       "          - setting2: 200\n"
                       "          - setting3: true\n"
                       "          + setting3: null\n"
                       "          + setting4: blah blah\n"
                       "          + setting5: {\n"
                       "                key5: value5\n"
                       "            }\n"
                       "            setting6: {\n"
                       "                doge: {\n"
                       "                  - wow: \n"
                       "                  + wow: so much\n"
                       "                }\n"
                       "                key: value\n"
                       "              + ops: vops\n"
                       "            }\n"
                       "        }\n"
                       "        group1: {\n"
                       "          - baz: bas\n"
                       "          + baz: bars\n"
                       "            foo: bar\n"
                       "          - nest: {\n"
                       "                key: value\n"
                       "            }\n"
                       "          + nest: str\n"
                       "        }\n"
                       "      - group2: {\n"
                       "            abc: 12345\n"
                       "            deep: {\n"
                       "                id: 45\n"
                       "            }\n"
                       "        }\n"
                       "      + group3: {\n"
                       "            deep: {\n"
                       "                id: {\n"
                       "                    number: 45\n"
                       "                }\n"
                       "            }\n"
                       "            fee: 100500\n"
                       "        }\n"
                       "    }")

    generated_output = generate_diff(file1, file2)
    print("Expected Output:\n", expected_output)
    print("\nGenerated Output:\n", generated_output)

    assert generated_output == expected_output
