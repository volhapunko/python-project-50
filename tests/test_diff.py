from gendiff import generate_diff
from gendiff.file_reader import read_file
    

def test_generate_diff_json_stylish():
    expected_result = read_file(
        'tests/test_data/expected_result.txt'
        )
    result = generate_diff(
        'tests/test_data/file1.json',
        'tests/test_data/file2.json'
        )

    assert result == expected_result


def test_generate_diff_yaml_stylish():
    expected_result = read_file(
        'tests/test_data/expected_result.txt'
        )
    result = generate_diff(
        'tests/test_data/file1.yml',
        'tests/test_data/file2.yml'
        )

    assert result == expected_result


def test_generate_diff_nested_json_stylish():
    expected_result = read_file(
        'tests/test_data/expected_nested.txt'
        )
    result = generate_diff(
        'tests/test_data/file3.json',
        'tests/test_data/file4.json'
        )

    assert result == expected_result


def test_generate_diff_nested_yaml_stylish():
    expected_result = read_file(
        'tests/test_data/expected_nested.txt'
        )
    result = generate_diff(
        'tests/test_data/file3.yml',
        'tests/test_data/file4.yml'
        )

    assert result == expected_result


def test_generate_diff_nested_json_plain():
    expected_result = read_file(
        'tests/test_data/expected_plain_nested.txt'
        )
    result = generate_diff(
        'tests/test_data/file3.json',
        'tests/test_data/file4.json',
        'plain'
        )

    assert result == expected_result


def test_generate_diff_nested_yaml_plain():
    expected_result = read_file(
        'tests/test_data/expected_plain_nested.txt'
        )
    result = generate_diff(
        'tests/test_data/file3.yml',
        'tests/test_data/file4.yml',
        'plain'
        )

    assert result == expected_result


def test_generate_diff_nested_json_json():
    expected_result = read_file(
        'tests/test_data/expected_json_nested.txt'
        )

    result = generate_diff(
        'tests/test_data/file3.json',
        'tests/test_data/file4.json',
        'json'
        )

    assert result == expected_result


def test_generate_diff_nested_yaml_json():
    expected_result = read_file(
        'tests/test_data/expected_json_nested.txt'
        )
    result = generate_diff(
        'tests/test_data/file3.yml',
        'tests/test_data/file4.yml',
        'json'
        )

    assert result == expected_result