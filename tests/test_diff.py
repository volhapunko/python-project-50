from gendiff.diff import generate_diff
from gendiff.file_reader import read_file
    

def test_generate_diff_json():
    data1 = read_file('tests/test_data/file1.json')
    data2 = read_file('tests/test_data/file2.json')
    expected_result = read_file(
        'tests/test_data/expected_result.txt'
        )

    result = generate_diff(data1, data2)

    assert result == expected_result


def test_generate_diff_yaml():
    data1 = read_file('tests/test_data/file1.yml')
    data2 = read_file('tests/test_data/file2.yml')
    expected_result = read_file(
        'tests/test_data/expected_result.txt'
        )

    result = generate_diff(data1, data2)

    assert result == expected_result