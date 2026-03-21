def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def format_stylish(diff, depth=1):
    lines = []
    indent = '    ' * depth

    for node in diff:
        key = node['key']
        status = node['status']
        value = node['value']

        if status == 'removed':
            lines.append(f'{indent[:-2]}  - {key}: {format_value(value)}')
        elif status == 'added':
            lines.append(f'{indent[:-2]}  + {key}: {format_value(value)}')
        elif status == 'unchanged':
            lines.append(f'{indent}    {key}: {format_value(value)}')
        elif status == 'changed':
            lines.append(f'{indent[:-2]}  - {key}: {
                format_value(node['old_value'])}')
            lines.append(f'{indent[:-2]}  + {key}: {
                format_value(node['new_value'])}')
        elif status == 'nested':
            lines.append(f'{indent}    {key}: {{')
            lines.extend(format_stylish(node['children'], depth + 1))
            lines.append(f'{indent}    }}')
    
    if depth == 1:
        return '\n'.join(['{'] + lines + ['}'])
    return lines