import pygame as pg
class shapes:
    def __init__(self):
        self.rect = pg.Rect(0, 0, 0, 0)

    def draw_rect(self, screen, left, top, width, height, colour):
        rect = pg.Rect(left, top, width, height)
        pg.draw.rect(screen, colour, rect)

    def get_rect(self):
        return self.rect

