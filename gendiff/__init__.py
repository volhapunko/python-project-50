from gendiff.builder.build_diff import build_diff
from gendiff.formatter.stylish import format_stylish


def generate_diff(data1, data2, format_name='stylish'):
    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)