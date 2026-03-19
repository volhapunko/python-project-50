def build_diff(data1, data2):
    diff = {}
    all_keys = sorted(set(data1.keys() | data2.keys()))

    for key in all_keys:
        if key in data1 and key not in data2:
            diff[key] = ('deleted', data1[key])
        elif key in data2 and key not in data1:
            diff[key] = ('added', data2[key])
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff[key] = ('nested', build_diff(data1[key], data2[key]))
        elif data1[key] == data2[key]:
            diff[key] = ('unchanged', data1[key])
        else:
            diff[key] = ('changed', data1[key], data2[key])
        
    return diff