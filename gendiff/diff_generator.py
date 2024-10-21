import json

def generate_diff(data1, data2):
    diff = []

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(f"    {key}: {data1[key]}")
            else:
                diff.append(f"  - {key}: {format_value(data1[key])}")
                diff.append(f"  + {key}: {format_value(data2[key])}")
        elif key in data1:
            diff.append(f"  - {key}: {format_value(data1[key])}")
        else:
            diff.append(f"  + {key}: {format_value(data2[key])}")

    return "{\n" + "\n".join(diff) + "\n}"

def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value
