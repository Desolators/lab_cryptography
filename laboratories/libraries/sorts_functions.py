from time import time

a = [55, 21, 45, 6, 0, 25, 46, 23, 86]


def merge_two_list():
    pass


def merge_sorte(list_unsorted):
    if len(list_unsorted) == 1:
        return list_unsorted
    left_list = merge_sorte(list_unsorted[0:len(list_unsorted) // 2])
    right_list = merge_sorte(list_unsorted[len(list_unsorted) // 2: len(list_unsorted)])
    return sorted(left_list + right_list)


a1 = time()
print(merge_sorte(a))
print(time() - a1)

# sort_1 = list_unsorted[0:len(list_unsorted) // 2]
# sort_2 = list_unsorted[len(list_unsorted) // 2: len(list_unsorted)]
#
