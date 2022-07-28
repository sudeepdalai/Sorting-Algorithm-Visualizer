import pygame

from pygame_modules.draw import draw
from algorithms.bubble_sort import bubble_sort
from algorithms.heap_sort import heap_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from pygame_modules.draw_information import DrawInformation
from helpers.common import generate_starting_list, refresh_rate_lookup


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 200

    lst = generate_starting_list(n, min_val, max_val)
    sorting = False
    draw_info = DrawInformation(800, 600, lst)
    ascending = True
    sorting_algo = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algo_generator = None

    while run:
        clock.tick(refresh_rate_lookup[sorting_algo_name])

        if sorting:
            try:
                next(sorting_algo_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algo_generator = sorting_algo(draw_info, ascending)
            elif event.key == pygame.K_a and sorting == False:
                ascending = True
            elif event.key == pygame.K_d and sorting == False:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algo = insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algo = bubble_sort
                sorting_algo_name = "Bubble Sort"
            elif event.key == pygame.K_s and not sorting:
                sorting_algo = selection_sort
                sorting_algo_name = "Selection Sort"
            elif event.key == pygame.K_h and not sorting:
                sorting_algo = heap_sort
                sorting_algo_name = "Heap Sort"

    pygame.quit()


if __name__ == '__main__':
    main()
