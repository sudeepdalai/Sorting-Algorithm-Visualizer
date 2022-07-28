from pygame_modules.draw_list import draw_list


def bubble_sort(draw_info, ascending=True):
    arr = draw_info.lst

    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            num1 = arr[j]
            num2 = arr[j+1]
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw_list(draw_info, {j: draw_info.GREEN,
                          j+1: draw_info.RED}, True)
                yield True

    return arr
