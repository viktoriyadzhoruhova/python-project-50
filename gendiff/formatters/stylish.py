def format_stylish(diff, depth=1):
    result = '{\n' + tree_view(diff, depth) + '\n}'
    return result

def tree_view(diff, depth=1):
    lines = []
    for node in diff:
        key = node['key']
        status = node['status']
        value = node.get('value') if status in ['added', 'removed', 'unchanged'] else (node.get('old_value'), node.get('new_value'))
        lines = create_formatted_line(lines, key, value, depth, status)
    return '\n'.join(lines)

def create_formatted_line(lines, key, value, depth, status):
    prefix = '  '
    if status == 'nested':
        indent = (4 * depth - 2) * ' '
        child_diff = tree_view(value, depth + 1)
        formatted_value = f'{{\n{child_diff}\n{indent}  }}'
        lines = add_indent_and_format(depth, lines, prefix, key, formatted_value)
    elif status == 'changed':
        lines = changed_data_diff(lines, value, depth, key)
    elif status == 'added':
        prefix = '+ '
        lines = add_indent_and_format(depth, lines, prefix, key, value)
    elif status == 'removed':
        prefix = '- '
        lines = add_indent_and_format(depth, lines, prefix, key, value)
    else:
        lines = add_indent_and_format(depth, lines, prefix, key, value)
    return lines

def add_indent_and_format(depth, lines, prefix, key, value):
    formatted_value = format_value(value, depth + 1)
    indent = (4 * depth - 2) * ' '
    lines.append(f"{indent}{prefix}{key}: {formatted_value}")
    return lines

def format_value(value, depth):
    if isinstance(value, dict):
        prefix = '  '
        lines = ['{']
        for key, val in value.items():
            formatted_value = format_value(val, depth + 1)
            lines = add_indent_and_format(depth, lines, prefix, key, formatted_value)
        indent = ' ' * (4 * (depth - 1))
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    return str(value)

def changed_data_diff(lines, value, depth, key):
    old_value, new_value = value
    old_new_pairs = [('- ', old_value), ('+ ', new_value)]
    for prefix, val in old_new_pairs:
        formatted_value = format_value(val, depth + 1)
        lines = add_indent_and_format(depth, lines, prefix, key, formatted_value)
    return lines
