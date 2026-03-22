from gendiff.formatters.plain import format_plain, format_plain_value


def test_format_plain_value():
    assert format_plain_value({'key': 'value'}) == '[complex value]'
    assert format_plain_value(True) == 'true'
    assert format_plain_value(False) == 'false'
    assert format_plain_value(None) == 'null'
    assert format_plain_value('value5') == "'value5'"
    assert format_plain_value(200) == '200'


def test_format_plain_removed():
    diff = [{'key': 'key', 'status': 'removed', 'value': 'value'}]
    result = format_plain(diff)
    assert result == "Property 'key' was removed"


def test_format_plain_added():
    diff = [{'key': 'key', 'status': 'added', 'value': 'value'}]
    result = format_plain(diff)
    assert result == "Property 'key' was added with value: 'value'"


def test_format_plain_changed():
    diff = [{
        'key': 'key',
        'status': 'changed',
        'old_value': 'old_val',
        'new_value': 'new_val'
    }]
    result = format_plain(diff)
    assert result == "Property 'key' was updated. \
From 'old_val' to 'new_val'"


def test_format_plain_nested():
    diff = [
        {
            'key': 'parent',
            'status': 'nested',
            'children': [
                {
                    'key': 'child',
                    'status': 'changed',
                    'old_value': 'old_val',
                    'new_value': 'new_val'
                }
            ]
        }
    ]
    result = format_plain(diff)
    assert result == "Property 'parent.child' was updated. \
From 'old_val' to 'new_val'"


def test_format_plain_nested_deep():
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
                            'status': 'added',
                            'value': 'value'
                        }
                    ]
                }
            ]
        }
    ]
    result = format_plain(diff)
    assert result == "Property 'a.b.c' was added with value: 'value'"


def test_format_plain_complex_value():
    diff = [{
        'key': 'key',
        'status': 'added',
        'value': {'nested': 'value'}
    }]
    result = format_plain(diff)
    assert result == "Property 'key' was added with value: [complex value]"