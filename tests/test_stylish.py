from gendiff.formatter.stylish import format_stylish


def test_format_stylish_removed():
    diff = [{'key': 'key', 'status': 'removed', 'value': 'value'}]

    result = format_stylish(diff)

    assert result == '{\n  - key: value\n}'


def test_format_stylish_added():
    diff = [{'key': 'key', 'status': 'added', 'value': 'value'}]

    result = format_stylish(diff)

    assert result == '{\n  + key: value\n}'


def test_format_stylish_unchanged():
    diff = [{'key': 'key', 'status': 'unchanged', 'value': 'value'}]

    result = format_stylish(diff)

    assert result == '{\n    key: value\n}'


def test_format_stylish_changed():
    diff = [
        {
            'key': 'key',
            'status': 'changed',
            'old_value': 'value1',
            'new_value': 'value2'
            }
    ]

    result = format_stylish(diff)

    assert result == '{\n  - key: value1\n  + key: value2\n}'


def test_format_stylish_nested():
    diff = [
        {
            'key': 'key',
            'status': 'nested',
            'children': [
                {
                    'key': 'key1',
                    'status': 'changed',
                    'old_value': 'value',
                    'new_value': 'value3'
                },
                {
                    'key': 'key2',
                    'status': 'unchanged',
                    'value': 'value2'
                }
            ]
        }
    ]

    result = format_stylish(diff)

    assert result == (
        '{\n'
        '    key: {\n'
        '      - key1: value\n'
        '      + key1: value3\n'
        '        key2: value2\n'
        '    }\n'
        '}'
    )