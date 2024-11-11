def format_plain(diff, path=''):
    lines = plain_formatter(diff, path)
    return "\n".join(lines)

def plain_formatter(diff, path=""):
    lines = []

    def add_line(status, value, full_key):
        actions = {
            "nested": lambda value, full_key: lines.extend(
                plain_formatter(value, full_key)
            ),
            "added": lambda value, full_key: lines.append(
                format_added_property(value, full_key)
            ),
            "removed": lambda value, full_key: lines.append(
                f"Property '{full_key}' was removed"
            ),
            "changed": lambda value, full_key: lines.append(
                format_changed_property(value, full_key)
            ),
            "unchanged": lambda value, full_key: None
        }
        action = actions.get(status)
        if action:
            action(value, full_key)

    for node in diff:
        key = node['key']
        status = node['status']
        full_key = create_full_key(path, key)
        value = (
            node.get('value')
            if status in ['added', 'removed', 'unchanged']
            else (node.get('old_value'), node.get('new_value'))
        )
        add_line(status, value, full_key)

    return lines

def create_full_key(path, key):
    return f"{path}.{key}" if path else key

def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return "null"
    return str(value).lower()

def format_added_property(value, full_key):
    value_description = format_value(value)
    return f"Property '{full_key}' was added with value: {value_description}"

def format_changed_property(value, full_key):
    old_value, new_value = value
    old_value = format_value(old_value)
    new_value = format_value(new_value)
    return f"Property '{full_key}' was updated. From {old_value} to {new_value}"
