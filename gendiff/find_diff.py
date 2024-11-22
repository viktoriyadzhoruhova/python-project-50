def find_diff(data1, data2):
    """
    Compares two dictionaries and returns their differences as a diff tree.

    Parameters:
    data1 (dict): First dictionary for comparison.
    data2 (dict): Second dictionary for comparison.

    Returns:
    dict: A dictionary representing the differences.
    """
    keys = sorted(set(data1.keys()).union(data2.keys()))
    diff = {}

    for key in keys:
        if key in data1 and key not in data2:
            diff[key] = ('removed', data1[key])
        elif key not in data1 and key in data2:
            diff[key] = ('added', data2[key])
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = ('nested', find_diff(data1[key], data2[key]))
        elif data1[key] == data2[key]:
            diff[key] = ('unchanged', data1[key])
        else:
            diff[key] = ('changed', (data1[key], data2[key]))

    return diff
