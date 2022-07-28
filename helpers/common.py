import random

refresh_rate_lookup = {
    "Bubble Sort": 90,
    "Selection Sort": 30,
    "Heap Sort": 30,
    "Insertion Sort": 90
}


def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst
