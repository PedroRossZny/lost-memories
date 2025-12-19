import pygame
from fonts import get_font
from visuals import place_border

# fonte base
base_font = get_font("jersey", 64)
base_font_big = get_font("jersey", 180)

def draw_title(surface, text="LOST MEMORIES", font=None, margin_top_percent=10, offset_y=0):
    """
    Função para centralizar título.
    :param surface: Surface do jogo.
    :param text: Texto do título.
    :param font: Fonte do título.
    :param margin_top_percent: Porcentagem de margem perânte o topo.
    :param offset_y: Deslocamento vertical opcional (para animações como 'breath').
    :return: Desenha o título centralizado horizontalmente, com margem superior em porcentagem.
    """
    if font is None:
        font = base_font_big

    # renderização do texto
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.centerx = surface.get_width() // 2
    text_rect.top = int(surface.get_height() * (margin_top_percent / 100)) + offset_y

    # borda
    place_border(surface, "images/edge1200x320.png", percent_x=50, margin_top_percent=1.5)

    # texto
    surface.blit(text_surface, text_rect)

def draw_options(surface, options, font=None, margin_bottom_percent=5, spacing=50):
    """
    Opções.
    :param surface: Surface do jogo.
    :param options: Lista de strings.
    :param font: Fonte usada (se None, usa base_font).
    :param margin_bottom_percent: Margem inferior em porcentagem da altura da tela.
    :param spacing: Espaçamento em pixels entre cada opção.
    :return: Desenha opções centralizadas horizontalmente, alinhadas de baixo para cima.
    """
    if font is None:
        font = base_font

    # último item da lista
    start_y = surface.get_height() - int(surface.get_height() * (margin_bottom_percent / 100))

    # borda
    place_border(surface, "images/edge400x300.png", percent_x=50, margin_bottom_percent=-0.5)

    for i, option in enumerate(reversed(options)):
        text_surface = font.render(option, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.centerx = surface.get_width() // 2
        text_rect.bottom = start_y - (i * spacing)

        surface.blit(text_surface, text_rect)

def draw_title_shadow(surface, text="LOST MEMORIES", font=None, margin_top_percent=10, offset_y=0):
    """
    Função para a sombra do título.
    :param surface: Surface do jogo.
    :param text: Texto da sombra do título.
    :param font: Fonte da sombra do título.
    :param margin_top_percent: Porcentagem de margem perânte o topo.
    :param offset_y: Deslocamento vertical opcional (para animações como 'breath').
    :return: Sombra do título.
    """
    if font is None:
        font = base_font_big

    # renderização do texto
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.centerx = surface.get_width() // 2
    text_rect.top = int(surface.get_height() * (margin_top_percent / 100)) + offset_y

    # texto
    surface.blit(text_surface, text_rect)

def draw_options_shadow(surface, options, font=None, margin_bottom_percent=5, spacing=50):
    """
    Sombra das opções.
    :param surface: Surface do jogo.
    :param options: Lista de strings.
    :param font: Fonte usada (se None, usa base_font).
    :param margin_bottom_percent: Margem inferior em porcentagem da altura da tela.
    :param spacing: Espaçamento em pixels entre cada opção.
    :return: Desenha opções centralizadas horizontalmente, alinhadas de baixo para cima.
    """
    if font is None:
        font = base_font

    # último item da lista de sombras
    start_y = surface.get_height() - int(surface.get_height() * margin_bottom_percent / 100)

    for i, option in enumerate(reversed(options)):
        text_surface = font.render(option, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.centerx = surface.get_width() // 2
        text_rect.bottom = start_y - (i * spacing)

        surface.blit(text_surface, text_rect)