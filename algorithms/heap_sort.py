from pygame_modules.draw_list import draw_list


def max_heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        max_heapify(arr, n, largest)


def min_heapify(arr, n, i):
    smallest = i  # Initialize smallest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    if l < n and arr[smallest] > arr[l]:
        smallest = l

    if r < n and arr[smallest] > arr[r]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # swap
        min_heapify(arr, n, smallest)


def heap_sort(draw_info, ascending=True):
    arr = draw_info.lst
    n = len(arr)
    heapify = max_heapify if ascending else min_heapify

    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
        draw_list(draw_info, {i: draw_info.GREEN,
                              0: draw_info.RED}, True)
        yield True
