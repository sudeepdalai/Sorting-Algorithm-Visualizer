import pygame

pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE
    GRADIENT = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]
    FONT = pygame.font.SysFont('comicsans', 20)
    LARGE_FONT = pygame.font.SysFont('comicsans', 25)

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst) -> None:
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Sorting Algorithm Visualizer')
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.max_value = max(lst)
        self.min_value = min(lst)

        self.block_width = (self.width - self.SIDE_PAD) // len(lst)
        self.block_height = (
            self.height - self.TOP_PAD) // (self.max_value - self.min_value)
        self.start_x = self.SIDE_PAD // 2
