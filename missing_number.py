def find_missing(list1, list2):
    if (not list1 and not list2) or (len(list1) == len(list2)):
        return 0
    result = list(set(sort_lists(list1,list2)[1]) - set(sort_lists(list1,list2)[0]))
    return result[0]


def sort_lists(list1, list2):
    if len(list1) < len(list2):
        return [list1, list2]
    else:
        return  [list2, list1]

print(find_missing([4, 6], [4, 6, 7]))