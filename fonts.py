import pygame

pygame.font.init()

FONTS = {
    "jersey": "fonts/Jersey10-Regular.ttf"
}

def get_font(name, size):
    return pygame.font.Font(FONTS[name], size)