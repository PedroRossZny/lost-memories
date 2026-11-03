import pygame
from functools import lru_cache


@lru_cache(maxsize=None)
def load_image(image_path):
    """Loads an image once and reuses it on later frames."""
    return pygame.image.load(image_path)

def place_border(surface, image_path, percent_x=50, margin_top_percent=None, margin_bottom_percent=None):
    """
    Posiciona uma borda na tela.
    :param surface: Surface do jogo.
    :param image_path: Caminho da imagem da borda.
    :param percent_x: Porcentagem horizontal (0 = esquerda, 100 = direita, 50 = centro).
    :param margin_top_percent: Margem superior em porcentagem da altura da tela.
    :param margin_bottom_percent: Margem inferior em porcentagem da altura da tela.
    :return: Rect da borda desenhada.
    """
    border_image = load_image(image_path)
    border_rect = border_image.get_rect()

    # posicionamento horizontal
    border_rect.centerx = int(surface.get_width() * (percent_x / 100))

    # posicionamento vertical
    if margin_top_percent is not None:
        border_rect.top = int(surface.get_height() * (margin_top_percent / 100))
    elif margin_bottom_percent is not None:
        border_rect.bottom = surface.get_height() - int(surface.get_height() * (margin_bottom_percent / 100))
    else:
        border_rect.centery = surface.get_height() // 2

    surface.blit(border_image, border_rect)

    return border_rect