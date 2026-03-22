from gendiff.builder.build_diff import build_diff
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.file_reader import read_file


def generate_diff(file1, file2, format_name='stylish'):
    data1 = read_file(file1)
    data2 = read_file(file2)
    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)