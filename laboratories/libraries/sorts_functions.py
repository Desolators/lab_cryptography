def merge_two_list(a, b):
    result = []
    i, j = 0, 0
    while a or b:
        if i == len(a):
            for end in range(j, len(b)):
                result.append(b[end])
            return result
        if j == len(b):
            for end in range(i, len(a)):
                result.append(a[end])
            return result
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
            continue
        if a[i] >= b[j]:
            result.append(b[j])
            j += 1
            continue


def merge_sorte(list_unsorted):
    if len(list_unsorted) == 1:
        return list_unsorted
    left_list = list(merge_sorte(list_unsorted[0:len(list_unsorted) // 2]))
    right_list = list(merge_sorte(list_unsorted[len(list_unsorted) // 2: len(list_unsorted)]))
    return merge_two_list(left_list, right_list)


def insert_sort(list_unsorted):
    for i in range(1, len(list_unsorted)):
        for j in range(i, 0, -1):
            if list_unsorted[j] < list_unsorted[j - 1]:
                list_unsorted[j], list_unsorted[j - 1] = list_unsorted[j - 1], list_unsorted[j]
    return list_unsorted


def choise_sort(list_unsorted):
    for i in range(0, len(list_unsorted) - 1):
        for j in range(i + 1, len(list_unsorted)):
            if list_unsorted[j] <= list_unsorted[i]:
                list_unsorted[i], list_unsorted[j] = list_unsorted[j], list_unsorted[i]
    return list_unsorted


def bubble_sort(list_unsorted):
    for i in range(1, len(list_unsorted)):
        for j in range(0, len(list_unsorted) - i):
            if list_unsorted[j] < list_unsorted[j + 1]:
                list_unsorted[j], list_unsorted[j + 1] = list_unsorted[j + 1], list_unsorted[j]
    return list_unsorted
