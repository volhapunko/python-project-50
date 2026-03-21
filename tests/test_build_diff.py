from gendiff.builder.build_diff import build_diff


def test_build_diff_removed():
    data1 = {'key': 'value'}
    data2 = {}

    result = build_diff(data1, data2)

    assert result == [
        {'key': 'key', 'status': 'removed', 'value': 'value'}
    ]


def test_build_diff_added():
    data1 = {}
    data2 = {'key': 'value'}

    result = build_diff(data1, data2)

    assert result == [
        {'key': 'key', 'status': 'added', 'value': 'value'}
    ]


def test_build_diff_unchanged():
    data1 = {'key': 'value'}
    data2 = {'key': 'value'}

    result = build_diff(data1, data2)

    assert result == [
        {'key': 'key', 'status': 'unchanged', 'value': 'value'}
    ]


def test_build_diff_changed():
    data1 = {'key': 'value1'}
    data2 = {'key': 'value2'}

    result = build_diff(data1, data2)

    assert result == [
        {'key': 'key', 'status': 'changed', 
'old_value': 'value1', 'new_value': 'value2'}
    ]


def test_build_diff_nested():
    data1 = {
        'key': {
            'key1': 'value',
            'key2': 'value2'
            }
    }
    data2 = {
        'key': {
            'key1': 'value3',
            'key2': 'value2'
            }
    }
    result = build_diff(data1, data2)

    assert result == [
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