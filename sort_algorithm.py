import numpy as np
import math
import psutil
import os


def selection_sort(data: list, progress_callback=None):
    """
    Selection sort.
    :param progress_callback:
    :param data:
    :return:
    """
    total = len(data) - 1
    for i in range(len(data) - 1):
        index = i
        for j in range(i + 1, len(data)):
            if data[index] > data[j]:
                index = j
        data[i], data[index] = data[index], data[i]
        if progress_callback is not None:
            progress_callback(i + 1, total, psutil.Process(os.getpid()).memory_info().rss / 1024)

    return data


def bubble_sort(data: list, progress_callback=None):
    """
    Bubble sort.
    :param progress_callback:
    :param data:
    :return:
    """
    total = len(data) - 1
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j + 1], data[j] = data[j], data[j + 1]
        if progress_callback is not None:
            progress_callback(i + 1, total, psutil.Process(os.getpid()).memory_info().rss / 1024)

    return data


def insertion_sort(data: list, progress_callback=None):
    """
    Insertion sort.
    :param progress_callback:
    :param data:
    :return:
    """
    total = len(data)
    for i in range(1, len(data)):
        for j in range(0, i):
            if data[i] < data[j]:
                data[j], data[i] = data[i], data[j]
        if progress_callback is not None:
            progress_callback(i + 1, total, psutil.Process(os.getpid()).memory_info().rss / 1024)

    return data


def merge_sort(data: list, progress_callback=None):
    """
    Merge sort
    :param progress_callback:
    :param data:
    :return:
    """
    if not hasattr(merge_sort, "progress"):
        merge_sort.progress = 0

    merge_sort.progress += 1
    total = 1000

    new_data = [0] * len(data)

    if progress_callback is not None:
        progress_callback(merge_sort.progress, total, psutil.Process(os.getpid()).memory_info().rss / 1024)
    if 2 == len(data):
        new_data = data if data[0] < data[1] else data[::-1]
    elif 2 < len(data):
        data[0: len(data) // 2] = merge_sort(data[0: len(data) // 2], progress_callback)
        data[len(data) // 2: len(data)] = merge_sort(data[len(data) // 2: len(data)], progress_callback)
        i, j, k = 0, len(data) // 2, 0
        while i != len(data) // 2 and j != len(data):
            if data[i] < data[j]:
                new_data[k] = data[i]
                i += 1
            else:
                new_data[k] = data[j]
                j += 1
            k += 1
        new_data[k: len(data)] = data[j: len(data)] if i == len(data) // 2 else data[i: len(data) // 2]
    else:
        new_data = data

    return new_data


def quick_sort(data: list, progress_callback=None):
    """
    Quick sort.
    :param progress_callback:
    :param data:
    :return:
    """
    if not hasattr(quick_sort, "progress"):
        quick_sort.progress = 0

    quick_sort.progress += 1
    total = 1000
    if progress_callback is not None:
        progress_callback(quick_sort.progress, total, psutil.Process(os.getpid()).memory_info().rss / 1024)

    if len(data) > 1:
        l, r, base = 0, len(data) - 1, data[0]
        while l < r:
            while base <= data[r] and l < r:
                r -= 1
            data[l] = data[r]
            while base > data[l] and l < r:
                l += 1
            data[r] = data[l]

        data[l] = base
        data[0: l] = quick_sort(data[0: l], progress_callback)
        data[r + 1: len(data)] = quick_sort(data[r + 1: len(data)], progress_callback)

    return data


def heap_sort(data: list, progress_callback=None):
    """
    Heap sort.
    :param progress_callback:
    :param progress_callback:
    :param data:
    :return:
    """
    progress = 0
    total = len(data) // 2 + len(data)
    for i in range(len(data) // 2 - 1, -1, -1):
        data = adjust_heap(data, i, len(data) - 1)
        progress += 1
        if progress_callback is not None:
            progress_callback(progress, total, psutil.Process(os.getpid()).memory_info().rss / 1024)

    for i in range(len(data) - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        data = adjust_heap(data, 0, i - 1)
        progress += 1
        if progress_callback is not None:
            progress_callback(progress, total, psutil.Process(os.getpid()).memory_info().rss / 1024)

    return data


def adjust_heap(data: list, root: int, end: int):
    """
    Adjusting the heap, only called by heap_sort function.
    :param data:
    :param root:
    :param end:
    :return:
    """
    child = root * 2 + 1
    while child <= end:
        if child < end and data[child] < data[child + 1]:
            child += 1
        if data[child] > data[root]:
            data[root], data[child] = data[child], data[root]
            root = child
            child = 2 * root + 1
        else:
            break

    return data


def shell_sort(data: list, progress_callback=None):
    """
    Shell sort.
    :param progress_callback:
    :param data:
    :return:
    """
    k = len(data) // 2
    progress = 0
    total = int(math.log(len(data), 2))
    while k > 0:
        for i in range(k, len(data)):
            while i >= k and data[i] < data[i - k]:
                data[i], data[i - k] = data[i - k], data[i]
                i -= k
        progress += 1
        if progress_callback is not None:
            progress_callback(progress, total, psutil.Process(os.getpid()).memory_info().rss / 1024)
        k //= 2

    return data


def counting_sort(data: list, progress_callback=None):
    """
    Counting sort.
    :param progress_callback:
    :param data:
    :return:
    """
    min_value = min(data)
    max_value = max(data)
    bucket = [0] * (max_value - min_value + 1)
    new_data = [0] * len(data)
    index = 0
    progress = 0
    total = len(data) * 2
    for i in range(len(data)):
        bucket[data[i] - min_value] += 1
        progress += 1
        if progress_callback is not None:
            progress_callback(progress, total, psutil.Process(os.getpid()).memory_info().rss / 1024)

    for i in range(len(bucket)):
        for j in range(bucket[i]):
            new_data[index] = i + min_value
            index += 1
            progress += 1
        if progress_callback is not None:
            progress_callback(progress, total, psutil.Process(os.getpid()).memory_info().rss / 1024)

    return new_data


def radix_sort(data: list, progress_callback=None):
    """
    Radix sort.
    :param progress_callback:
    :param data:
    :return:
    """
    max_value = max(data)
    bucket = [[] for i in range(10)]
    digit_number = len(str(max_value))
    i = 1
    progress = 0
    total = digit_number
    while i <= digit_number:
        for j in data:
            bucket[j % (10 ** i) // (10 ** (i - 1))].append(j)
        data.clear()
        for l in bucket:
            data.extend(l)

        bucket = [[] for i in range(10)]

        i += 1
        progress += 1

        if progress_callback is not None:
            progress_callback(progress, total, psutil.Process(os.getpid()).memory_info().rss / 1024)

    return data


def check(data: list):
    """
    To check the data is sorted or not.
    :param data:
    :param length:
    :return:
    """

    is_sorted = True
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            is_sorted = False

    return is_sorted


def main():
    # i: progress, j: total_progress, k: memory
    def p(i, j, k):
        print(k)
        # print(i, j)
        a = 0
    print(psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024)
    d = list(np.random.randint(0, 1000, 100000))
    d = merge_sort(list(d), p)
    print(d)
    print(check(d))
    print(psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024)


if __name__ == '__main__':
    main()
