import pygame
from animations import fade_in
from fonts import get_font
from menu import draw_title, draw_options

pygame.init()

# cor de fundo do menu
vine = pygame.Color(140, 10, 30)

# fonte principal
jersey_font = get_font("jersey", 64)

# fonte para títulos
jersey_font_big = get_font("jersey", 180)

# fonte pequena
jersey_font_small = get_font("jersey", 45)

# janela do jogo
win = pygame.Window(size=(1280, 720))
surf = win.get_surface()

# animação antes do menu
fade_in(win, vine, duration=8, step=5, title="LOST MEMORIES", font=jersey_font_big, font_percent=20, margin_top_percent=10)

# jogo rodando
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surf.fill(vine)

    # título
    draw_title(surf, text="LOST MEMORIES", font=jersey_font_big, margin_top_percent=10)

    # opções
    menu_options = ["Play", "Settings", "Controls", "Credits", "Exit"]
    draw_options(surf, menu_options, font=jersey_font_small, margin_bottom_percent=1, spacing=45)

    win.flip()

pygame.quit()