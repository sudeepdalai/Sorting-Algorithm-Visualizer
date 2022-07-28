from pygame_modules.draw_list import draw_list


def selection_sort(draw_info, ascending=True):
    arr = draw_info.lst

    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if (arr[min_idx] > arr[j] and ascending) or (arr[min_idx] < arr[j] and not ascending):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw_list(draw_info, {min_idx: draw_info.GREEN,
                              i: draw_info.RED}, True)
        yield True

    return arr
