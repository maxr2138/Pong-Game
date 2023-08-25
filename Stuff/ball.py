import pygame as pg
class ball():
    def circle(self, screen, ball_colour, radius, location):
        ball = pg.draw.circle(screen, ball_colour, location, radius)
