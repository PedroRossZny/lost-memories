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

def draw_option(surface, text, text_color, shadow_color, text_font, shadow_font, shadow_distance, margin_bottom_percent, spacing_bottom, percent_x, index=0, hover_color=(255, 255, 150)):
    """
    Desenha uma única opção com sombra.
    :param surface: Surface do jogo.
    :param text: Texto da opção.
    :param text_color: Cor RGB do texto.
    :param shadow_color: Cor RGB da sombra.
    :param text_font: Fonte do texto.
    :param shadow_font: Fonte da sombra.
    :param shadow_distance: Distância vertical da sombra em pixels.
    :param margin_bottom_percent: Margem inferior em porcentagem da altura da tela.
    :param spacing_bottom: Espaçamento em pixels entre opções.
    :param percent_x: Posição horizontal em porcentagem (0 esquerda, 50 centro, 100 direita).
    :param index: Índice da opção (0 = última, 1 = acima, etc).
    :param hover_color: Cor do texto no hover.
    :return: Opção ou lista de opções na tela.
    """
    # posição base (última opção)
    start_y = surface.get_height() - int(surface.get_height() * (margin_bottom_percent / 100))
    option_y = start_y - (index * spacing_bottom)

    # posição horizontal
    center_x = int(surface.get_width() * (percent_x / 100))

    # rect base para detectar hover
    text_surface =  text_font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = center_x
    text_rect.bottom = option_y

    mouse_pos = pygame.mouse.get_pos()
    is_hover = text_rect.collidepoint(mouse_pos)

    if is_hover:
        # render sombra maior
        shadow_surface = shadow_font.render(text, True, shadow_color)
        shadow_rect = shadow_surface.get_rect()
        shadow_rect.centerx =  center_x
        shadow_rect.bottom = option_y + shadow_distance
        surface.blit(shadow_surface, shadow_rect)

        # render texto maior e cor de hover
        text_surface = shadow_font.render(text, True, hover_color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = center_x
        text_rect.bottom = option_y
        surface.blit(text_surface, text_rect)
    else:
        # render sombra normal
        shadow_surface =  shadow_font.render(text, True, shadow_color)
        shadow_rect = shadow_surface.get_rect()
        shadow_rect.centerx = center_x
        shadow_rect.bottom = option_y + shadow_distance
        surface.blit(shadow_surface, shadow_rect)

        # render texto normal
        text_surface = text_font.render(text, True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.centerx = center_x
        text_rect.bottom = option_y
        surface.blit(text_surface, text_rect)