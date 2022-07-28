import pygame
from pygame_modules.draw_list import draw_list


def draw(draw_info, sorting_algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(
        f"{sorting_algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.GREEN)
    draw_info.window.blit(
        title, (draw_info.width/2 - title.get_width()/2, 5))

    controls = draw_info.FONT.render(
        "R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(
        controls, (draw_info.width/2 - controls.get_width()/2, 35))
    controls = draw_info.FONT.render(
        "I - Insertion Sort | B - Bubble Sort | S - Selection Sort | H - Heap Sort", 1, draw_info.BLACK)
    draw_info.window.blit(
        controls, (draw_info.width/2 - controls.get_width()/2, 65))

    draw_list(draw_info)
    pygame.display.update()
