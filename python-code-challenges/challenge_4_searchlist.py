"""
Challenge 4: Search a list
"""


def search_list(input_list, search_term):
    """
    Search for an item in list
    """
    result_list = []
    for index, _input in enumerate(input_list):
        if _input == search_term:
            result_list.append(index)
            continue
            
        if isinstance(_input, list):
            inner_result_list = search_list(_input, search_term)
            for inner_result in inner_result_list:
                print(inner_result)
                result = [index]
                if isinstance(inner_result, list):
                    result.extend(inner_result)
                else:
                    result.append(inner_result)
                result_list.append(result)
    return result_list


print(search_list([
    1,
    2,
    3,
    [
        2,
        2,
        [
            1,
            2
        ]
    ],
    2,
    [
        1,
        1,
        1,
        [
            2,
            [
                1,
                2
            ]
        ]
    ]
], 2))
