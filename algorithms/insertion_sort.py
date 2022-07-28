from pygame_modules.draw_list import draw_list


def insertion_sort(draw_info, ascending=True):
    arr = draw_info.lst

    for i in range(1, len(arr)):
        current = arr[i]

        while True:
            ascending_sort = i > 0 and arr[i - 1] > current and ascending
            descending_sort = i > 0 and arr[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            arr[i] = arr[i - 1]
            i = i - 1
            arr[i] = current
            draw_list(draw_info, {i - 1: draw_info.GREEN,
                      i: draw_info.RED}, True)
            yield True

    return arr
