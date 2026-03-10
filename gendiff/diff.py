def generate_diff(data1, data2):
    result = []
    result.append('{')

    all_keys = sorted(set(data1.keys() | data2.keys()))
    for key in all_keys:
        if key not in data2:
            result.append(f'  - {key}: {data1[key]}')
        elif key not in data1:
            result.append(f'  + {key}: {data2[key]}')
        elif data1[key] == data2[key]:
            result.append(f'    {key}: {data1[key]}')
        else:
            result.append(f'  - {key}: {data1[key]}')
            result.append(f'  + {key}: {data2[key]}')
        
    result.append('}')

    result_str = '\n'.join(result)
    return result_str
