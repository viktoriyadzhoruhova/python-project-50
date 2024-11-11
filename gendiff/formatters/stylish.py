def format_stylish(diff, depth=1):
    lines = ['{']

    for node in diff:
        key = node['key']
        status = node['status']
        current_indent = '    ' * (depth - 1)

        if status == 'removed':
            lines.append(
                f"{current_indent}  - {key}: {format_value(node['value'])}"
            )
        elif status == 'added':
            lines.append(
                f"{current_indent}  + {key}: {format_value(node['value'])}"
            )
        elif status == 'changed':
            lines.append(
                f"{current_indent}  - {key}: {format_value(node['old_value'])}"
            )
            lines.append(
                f"{current_indent}  + {key}: {format_value(node['new_value'])}"
            )
        elif status == 'nested':
            children = format_stylish(node['children'], depth + 1)
            lines.append(
                f"{current_indent}    {key}: {children}"
            )
        else:
            lines.append(
                f"{current_indent}    {key}: {format_value(node['value'])}"
            )

    lines.append(f"{current_indent}}}")
    return '\n'.join(lines)

def format_value(value):
    """Форматирует значение для корректного вывода."""
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        lines = ['{']
        for k, v in value.items():
            lines.append(f"    {k}: {format_value(v)}")
        lines.append('}')
        return '\n'.join(lines)
    elif isinstance(value, str):
        return value
    return str(value)
