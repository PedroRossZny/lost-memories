import pygame
from animations import fade_in

pygame.init()

# cor de fundo do menu
vine = pygame.Color(140, 10, 30)

# janela do jogo
win = pygame.Window(size=(1280, 720))
surf = win.get_surface()

# animação antes do menu
fade_in(win, vine, duration=8, step=5, title="LOST MEMORIES", font_percent=20, margin_top_percent=10)

# jogo rodando
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surf.fill(vine)
    win.flip()

pygame.quit()