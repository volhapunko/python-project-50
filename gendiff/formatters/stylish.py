def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def format_dict(value, depth):
    if not isinstance(value, dict):
        return format_value(value)
    
    lines = []
    indent = '    ' * depth
    for key, val in (value.items()):
        lines.append(f"{indent}    {key}: {format_dict(val, depth + 1)}")
    
    if not lines:
        return '{}'
    return '{\n' + '\n'.join(lines) + f'\n{indent}}}'


def format_stylish(diff, depth=1):
    lines = []
    indent = '    ' * depth

    for node in diff:
        key = node['key']
        status = node['status']

        if status == 'removed':
            val = format_dict(node['value'], depth)
            lines.append(f"{'    ' * (depth - 1)}  - {key}: {val}")
        elif status == 'added':
            val = format_dict(node['value'], depth)
            lines.append(f"{'    ' * (depth - 1)}  + {key}: {val}")
        elif status == 'unchanged':
            lines.append(f"{indent}{key}: {format_value(node['value'])}")
        elif status == 'changed':
            old_val = format_dict(node['old_value'], depth)
            new_val = format_dict(node['new_value'], depth)
            lines.append(f"{'    ' * (depth - 1)}  - {key}: {old_val}")
            lines.append(f"{'    ' * (depth - 1)}  + {key}: {new_val}")
        elif status == 'nested':
            lines.append(f"{indent}{key}: {{")
            lines.extend(format_stylish(node['children'], depth + 1))
            lines.append(f"{indent}}}")
    
    if depth == 1:
        return '\n'.join(['{'] + lines + ['}'])
    return lines