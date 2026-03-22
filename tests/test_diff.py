from gendiff import generate_diff
from gendiff.file_reader import read_file
    

def test_generate_diff_json_stylish():
    data1 = read_file('tests/test_data/file1.json')
    data2 = read_file('tests/test_data/file2.json')
    expected_result = read_file(
        'tests/test_data/expected_result.txt'
        )

    result = generate_diff(data1, data2)

    assert result == expected_result


def test_generate_diff_yaml_stylish():
    data1 = read_file('tests/test_data/file1.yml')
    data2 = read_file('tests/test_data/file2.yml')
    expected_result = read_file(
        'tests/test_data/expected_result.txt'
        )

    result = generate_diff(data1, data2)

    assert result == expected_result


def test_generate_diff_nested_json_stylish():
    data1 = read_file('tests/test_data/file3.json')
    data2 = read_file('tests/test_data/file4.json')
    expected_result = read_file(
        'tests/test_data/expected_nested.txt'
        )

    result = generate_diff(data1, data2)

    assert result == expected_result


def test_generate_diff_nested_yaml_stylish():
    data1 = read_file('tests/test_data/file3.yml')
    data2 = read_file('tests/test_data/file4.yml')
    expected_result = read_file(
        'tests/test_data/expected_nested.txt'
        )

    result = generate_diff(data1, data2)

    assert result == expected_result


def test_generate_diff_nested_json_plain():
    data1 = read_file('tests/test_data/file3.json')
    data2 = read_file('tests/test_data/file4.json')
    expected_result = read_file(
        'tests/test_data/expected_plain_nested.txt'
        )

    result = generate_diff(data1, data2, 'plain')

    assert result == expected_result


def test_generate_diff_nested_yaml_plain():
    data1 = read_file('tests/test_data/file3.yml')
    data2 = read_file('tests/test_data/file4.yml')
    expected_result = read_file(
        'tests/test_data/expected_plain_nested.txt'
        )

    result = generate_diff(data1, data2, 'plain')

    assert result == expected_result


def test_generate_diff_nested_json_json():
    data1 = read_file('tests/test_data/file3.json')
    data2 = read_file('tests/test_data/file4.json')
    expected_result = read_file(
        'tests/test_data/expected_json_nested.txt'
        )

    result = generate_diff(data1, data2, 'json')

    assert result == expected_result


def test_generate_diff_nested_yaml_json():
    data1 = read_file('tests/test_data/file3.yml')
    data2 = read_file('tests/test_data/file4.yml')
    expected_result = read_file(
        'tests/test_data/expected_json_nested.txt'
        )

    result = generate_diff(data1, data2, 'json')

    assert result == expected_result