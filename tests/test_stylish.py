from gendiff.formatters.stylish import format_stylish


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


def test_format_stylish_nested_deep():
    diff = [
        {
            'key': 'a',
            'status': 'nested',
            'children': [
                {
                    'key': 'b',
                    'status': 'nested',
                    'children': [
                        {
                            'key': 'c',
                            'status': 'changed',
                            'old_value': 'old_val',
                            'new_value': 'new_val'
                        }
                    ]
                }
            ]
        }
    ]

    result = format_stylish(diff)

    assert result == (
        '{\n'
        '    a: {\n'
        '        b: {\n'
        '          - c: old_val\n'
        '          + c: new_val\n'
        '        }\n'
        '    }\n'
        '}'
    )


def test_format_stylish_empty():
    diff = []
    result = format_stylish(diff)
    assert result == '{\n}'