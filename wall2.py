import pygame

class Wall2:
    def __init__(self, x=0, y=0, width=50, height=50):  # x, y, 가로, 세로
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def SetSize(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, display_surface, color):
        pygame.draw.rect(display_surface, color, (self.x, self.y, self.width, self.height))