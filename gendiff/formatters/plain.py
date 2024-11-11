def format_plain(diff, path=''):
    lines = []

    for node in diff:
        key = node['key']
        full_path = f"{path}.{key}" if path else key
        status = node['status']

        if status == 'removed':
            lines.append(f"Property '{full_path}' was removed")
        elif status == 'added':
            value = format_value_plain(node['value'])
            lines.append(f"Property '{full_path}' was added with value: {value}")
        elif status == 'changed':
            old_value = format_value_plain(node['old_value'])
            new_value = format_value_plain(node['new_value'])
            lines.append(f"Property '{full_path}' was updated. From {old_value} to {new_value}")
        elif status == 'nested':
            children = format_plain(node['children'], full_path)
            lines.extend(children)

    result = "\n".join(lines)
    return result

def format_value_plain(value):
    """Форматирует значение для plain представления."""
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)
