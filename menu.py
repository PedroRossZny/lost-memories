import pygame
from fonts import get_font
from visuals import draw_edge

# fonte base
base_font = get_font("jersey", 64)
base_font_big = get_font("jersey", 180)

def draw_title(surface, text="LOST MEMORIES", font=None, margin_top_percent=10):
    """
    Função para centralizar título.
    :param surface: Surface do jogo.
    :param text: Texto do título.
    :param font: Fonte do título.
    :param margin_top_percent: Porcentagem de margem perânte o topo.
    :return: Desenha o título centralizado horizontalmente, com margem superior em porcentagem.
    """
    if font is None:
        font = base_font_big

    # renderização do texto
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.centerx = surface.get_width() // 2
    text_rect.top = int(surface.get_height() * (margin_top_percent / 100))

    # borda
    draw_edge(surface, text_rect.width, text_rect.height, margin_h=50, margin_v=20, align="center", margin_top_percent=margin_top_percent)

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

    longest = max(options, key=lambda opt: font.size(opt)[0])
    longest_width, _ = font.size(longest)

    # borda
    draw_edge(surface, longest_width, longest_width, margin_h=50, margin_v=0, align="center", margin_bottom_percent=margin_bottom_percent)

    # último item da lista
    start_y = surface.get_height() - int(surface.get_height() * (margin_bottom_percent / 100))

    for i, option in enumerate(reversed(options)):
        text_surface = font.render(option, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.centerx = surface.get_width() // 2
        text_rect.bottom = start_y - (i * spacing)

        surface.blit(text_surface, text_rect)
