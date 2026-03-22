def format_plain_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff, path=''):
    lines = []
    for node in diff:
        if path:
            current_path = f"{path}.{node['key']}"
        else:
            current_path = node['key']

        if node['status'] == 'nested':
            lines.extend(format_plain(node['children'], current_path))

        elif node['status'] == 'removed':
            lines.append(f"Property '{current_path}' was removed")

        elif node['status'] == 'added':
            value = format_plain_value(node['value'])
            lines.append(f"Property '{current_path}' was added with value: {value}")
        elif node['status'] == 'changed':
            old_val = format_plain_value(node['old_value'])
            new_val = format_plain_value(node['new_value'])
            lines.append(f"Property '{current_path}' was updated. \
From {old_val} to {new_val}")
    return '\n'.join(lines)