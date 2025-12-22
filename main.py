import pygame
from animations import fade_in, breath_step
from fonts import get_font
from menu import draw_title, draw_title_shadow, draw_option
from visuals import place_border

pygame.init()

# cor de fundo do menu
vine = pygame.Color(140, 10, 30)

# fonte principal
jersey_font = get_font("jersey", 64)
jersey_font_shadow = get_font("jersey", 70)

# fonte para títulos
jersey_font_big = get_font("jersey", 180)
jersey_font_big_shadow = get_font("jersey", 186)

# fonte pequena
jersey_font_small = get_font("jersey", 45)
jersey_font_small_shadow = get_font("jersey", 47)

# janela do jogo
win = pygame.Window(size=(1280, 720))
surf = win.get_surface()

# relógio para controlar FPS
clock = pygame.time.Clock()

# animação antes do menu
fade_in(win, vine, duration=1, step=5, title="LOST MEMORIES", font=jersey_font_big, font_percent=20, margin_top_percent=10)

# variáveis de animação breath
step = 0
pixels = 2
hold = 10

# jogo rodando
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surf.fill(vine)

    # animação de deslocamento de texo
    offset = breath_step(step, pixels=pixels, hold=hold)
    step += 1

    # título
    draw_title_shadow(surf, text="LOST MEMORIES", font=jersey_font_big_shadow, margin_top_percent=11, offset_y=offset)
    draw_title(surf, text="LOST MEMORIES", font=jersey_font_big, margin_top_percent=10, offset_y=offset)

    # borda das opções
    place_border(surf, "images/edge443x332.png", percent_x=50, margin_bottom_percent=-1)

    # opções
    menu_options = ["Play", "Settings", "Controls", "Credits", "Exit"]
    for i, option in enumerate(reversed(menu_options)):
        draw_option(surf, text=option, text_color=(255, 255, 255), shadow_color=(0, 0, 0), text_font=jersey_font_small, shadow_font=jersey_font_small_shadow, shadow_distance=6, margin_bottom_percent=5.3, spacing_bottom=49, percent_x=50, index=i, hover_color=(255, 255, 150))

    win.flip()
    clock.tick(60) # 60 FPS

pygame.quit()