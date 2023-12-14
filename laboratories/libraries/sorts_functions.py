from time import time

list_list = [55, 21, 45, 6, 0, 25, 46, 23, 86]


def merge_two_list(a, b):
    return sorted(a + b)


def merge_sorte(list_unsorted):
    if len(list_unsorted) == 1:
        return list_unsorted
    left_list = merge_sorte(list_unsorted[0:len(list_unsorted) // 2])
    right_list = merge_sorte(list_unsorted[len(list_unsorted) // 2: len(list_unsorted)])
    return merge_two_list(left_list, right_list)


time_go = time()
print(merge_sorte(list_list))
print(time() - time_go)
