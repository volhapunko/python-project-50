import json

from gendiff import generate_diff


def read_file(file_path):
    with open(file_path) as f:
        return json.load(f)
    

def read_expected_result(file_path):
    with open(file_path) as f:
        return f.read()
    

def test_generate_diff():
    data1 = read_file('tests/test_data/file1.json')
    data2 = read_file('tests/test_data/file2.json')
    expected_result = read_expected_result(
        'tests/test_data/expected_result.txt'
        )

    result = generate_diff(data1, data2)

    assert result == expected_result