import json

from gendiff.formatters.json import format_json


def test_format_json_removed():
    diff = [{'key': 'key', 'status': 'removed', 'value': 'value'}]
    result = format_json(diff)
    expected = json.dumps(diff, indent=2)
    assert result == expected


def test_format_json_added():
    diff = [{'key': 'key', 'status': 'added', 'value': 'value'}]
    result = format_json(diff)
    expected = json.dumps(diff, indent=2)
    assert result == expected


def test_format_json_unchanged():
    diff = [{'key': 'key', 'status': 'unchanged', 'value': 'value'}]
    result = format_json(diff)
    expected = json.dumps(diff, indent=2)
    assert result == expected


def test_format_json_changed():
    diff = [{
        'key': 'key',
        'status': 'changed',
        'old_value': 'old_val',
        'new_value': 'new_val'
    }]
    result = format_json(diff)
    expected = json.dumps(diff, indent=2)
    assert result == expected


def test_format_json_nested():
    diff = [
        {
            'key': 'parent',
            'status': 'nested',
            'children': [
                {'key': 'child', 'status': 'unchanged', 'value': 'value'}
            ]
        }
    ]
    result = format_json(diff)
    expected = json.dumps(diff, indent=2)
    assert result == expected


def test_format_json_nested_deep():
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
    result = format_json(diff)
    expected = json.dumps(diff, indent=2)
    assert result == expected