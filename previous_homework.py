from task_2 import logger


@logger('previous.log')
def get_flat_list(list_of_lists):
    result = []

    for inner_list in list_of_lists:
        for item in inner_list:
            result.append(item)

    return result


@logger('previous.log')
def get_recursive_flat_list(data):
    result = []

    for item in data:
        if isinstance(item, list):
            result.extend(get_recursive_flat_list(item))
        else:
            result.append(item)

    return result


def test_previous():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    assert get_flat_list(list_of_lists_1) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None
    ]

    assert get_recursive_flat_list(list_of_lists_2) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'
    ]


if __name__ == '__main__':
    test_previous()
