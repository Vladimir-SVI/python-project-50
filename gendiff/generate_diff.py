import json


def generate_diff(file1, file2):


    def append_in_list(key, value):
        if value == True:
            value = 'true'
        if value == False:
            value = 'false'
        str_key_value = f'  {key}: {value}'
        work_list.append(str_key_value)
    

    work_list = []

    with open(file1, "r") as f1:
        dict1 = json.load(f1)
    with open(file2, "r") as f2:
        dict2 = json.load(f2)

    dict1_keys = sorted(dict1.keys())
    dict2_keys = sorted(dict2.keys())
    all_keys = sorted(set(dict1_keys + dict2_keys))

    for i in all_keys:
        if i in dict1_keys and i not in dict2_keys:
            append_in_list('- ' + i, dict1[i])
        if i in dict1_keys and i in dict2_keys:
            if dict1[i] == dict2[i]:
                append_in_list(i, dict1[i])
            else:
                append_in_list('- ' + i, dict1[i])
                append_in_list('+ ' + i, dict2[i])
        if i not in dict1_keys and i in dict2_keys:
            append_in_list('+ ' + i, dict2[i])
            
    list_result = []
    work_list.insert(0, '{')
    for i in work_list:
        list_result.append(i)
        list_result.append('\n')
    list_result.append('}')

    result = ''.join(list_result)
    print(result)
