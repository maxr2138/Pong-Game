import pygame as pg
pg.init()
class Button:
    def __init__(self,screen, text, font, font_colour, colour, new_colour, button_dimensions):
        self.text = text
        self.font = font
        self.colour = colour
        self.screen = screen
        self.button_dimensions = button_dimensions
        self.new_colour = new_colour
        self.font_colour = font_colour

    def create_button(self):
        x,y = pg.mouse.get_pos()

        image = self.font.render(self.text, True, self.font_colour)
        self.button = pg.Rect(self.button_dimensions[0], self.button_dimensions[1]
                         , self.button_dimensions[2], self.button_dimensions[3])  # x position, y position, rectangle width, rectangle height
        if self.button_dimensions[0] <= x <= self.button_dimensions[0] + self.button_dimensions[2] and self.button_dimensions[1] <= y <= self.button_dimensions[1] + self.button_dimensions[3]:
            pg.draw.rect(self.screen, self.new_colour, self.button)
        else:
            pg.draw.rect(self.screen, self.colour, self.button)
        self.screen.blit(image, ((self.button_dimensions[0] + 5), (self.button_dimensions[1] + 3)))

    def return_button(self):
        return self.button
    def draw_rect(self):
        pass

















# pg.draw.rect(screen, colour, self.rect)