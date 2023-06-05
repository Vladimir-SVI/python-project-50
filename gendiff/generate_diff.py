from gendiff.append_in_list import append_in_list
from gendiff.parsing import parse


def generate_diff(file1, file2):
    work_list = []
    # with open(file1, "r") as f1:
    #     dict1 = json.load(f1)
    # with open(file2, "r") as f2:
    #     dict2 = json.load(f2)
    dict1 = parse(file1)
    dict2 = parse(file2)

    dict1_keys = sorted(dict1.keys())
    dict2_keys = sorted(dict2.keys())
    all_keys = sorted(set(dict1_keys + dict2_keys))

    for i in all_keys:
        if i in dict1_keys and i not in dict2_keys:
            append_in_list('- ' + i, dict1[i], work_list)
        if i in dict1_keys and i in dict2_keys:
            if dict1[i] == dict2[i]:
                append_in_list('  ' + i, dict1[i], work_list)
            else:
                append_in_list('- ' + i, dict1[i], work_list)
                append_in_list('+ ' + i, dict2[i], work_list)
        if i not in dict1_keys and i in dict2_keys:
            append_in_list('+ ' + i, dict2[i], work_list)

    list_result = []
    work_list.insert(0, '{')
    for i in work_list:
        list_result.append(i)
        list_result.append('\n')
    list_result.append('}')

    result = ''.join(list_result)
    return result
