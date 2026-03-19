def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)

def format_stylish(diff, depth=1):
    lines = []
    indent = '    ' * depth

    for key in diff:
        status, *vals = diff[key]

        if status == 'deleted':
            lines.append(f'{indent[:-2]}  - {key}: {format_value(vals[0])}')
        elif status == 'added':
            lines.append(f'{indent[:-2]}  + {key}: {format_value(vals[0])}')
        elif status == 'unchanged':
            lines.append(f'{indent}    {key}: {format_value(vals[0])}')
        elif status == 'changed':
            lines.append(f'{indent[:-2]}  - {key}: {format_value(vals[0])}')
            lines.append(f'{indent[:-2]}  + {key}: {format_value(vals[1])}')
        elif status == 'nested':
            lines.append(f'{indent}    {key}: {{')
            lines.extend(format_stylish(vals[0], depth + 1))
            lines.append(f'{indent}    }}')
    
    if depth == 1:
        return '\n'.join(['{'] + lines + ['}'])
    return lines