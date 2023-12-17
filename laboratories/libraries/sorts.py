from sys import set_int_max_str_digits
set_int_max_str_digits(0)


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


def count_elem_numbers_and_sort(file):
    unsorted = read_str(file)
    list_unsorted = list(unsorted[0])
    unique_numbers = len(set(list_unsorted))
    count = [0] * unique_numbers
    difference = int(min(list_unsorted))
    for i in list_unsorted:
        count[int(i) - difference] += 1
    currentpos, list_sorted = 0, list_unsorted
    for val in range(0, unique_numbers):
        for i in range(count[val]):
            list_sorted[currentpos] = val + difference
            currentpos += 1
    return count, list_sorted


def read_str(file):
    with open(file) as file:
        lines = file.readlines()
        return lines
