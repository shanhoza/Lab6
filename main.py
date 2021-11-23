inp = [1, 4, 5], [1, 3, 4], [2, 6]


def merge(lists):
    new_list = sum(lists, [])
    new_list.sort()
    return new_list


print(merge(inp))
