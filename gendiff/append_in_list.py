def append_in_list(key, value, work_list):
    if value is True:
        value = 'true'
    if value is False:
        value = 'false'
    str_key_value = f'  {key}: {value}'
    work_list.append(str_key_value)
