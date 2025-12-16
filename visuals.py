import pygame

# imagem da borda
EDGE_IMAGE = pygame.image.load("images/edge64x64.png")

def draw_edge(surface, width, height, margin_h=0, margin_v=0, align="center", margin_top_percent=None, margin_bottom_percent=None):
    """
    Desenha uma borda flexível atrás de um elemento.
    :param surface: Surface do jogo.
    :param width: Largura do elemento (ex.: texto).
    :param height: Altura do elemento.
    :param margin_h: Padding horizontal (px).
    :param margin_v: Padding vertical (px).
    :param align: Posicionamento horizontal ("center", "left", "right").
    :param margin_top_percent: Margem superior (% da tela).
    :param margin_bottom_percent: Margem inferior (% da tela).
    :return: Rect da borda desenhada.
    """
    final_width = width + (margin_h * 2)
    final_height = height + (margin_v * 2)

    edge_scaled = pygame.transform.scale(EDGE_IMAGE, (final_width, final_height))
    edge_rect = edge_scaled.get_rect()

    # posicionamento horizontal
    if align == "center":
        edge_rect.centerx = surface.get_width() // 2
    elif align == "left":
        edge_rect.left = margin_h
    elif align == "right":
        edge_rect.right = surface.get_width() - margin_h

    # posicionamento vertical
    if margin_top_percent is not None:
        edge_rect.top = int(surface.get_height() * (margin_top_percent / 100))
    elif margin_bottom_percent is not None:
        edge_rect.bottom = surface.get_height() - int(surface.get_height() * (margin_bottom_percent / 100))

    # desenha a borda
    surface.blit(edge_scaled, edge_rect)

    return edge_rect

