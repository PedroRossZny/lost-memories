import pygame
import time

def fade_in(window, color, duration=2.0, step=5, title=None, font=None, font_percent=20, margin_top_percent=10):
    """
    Executa uma animação de fade-in na janela.
    :param window: Window (pygame.Window): objeto da janela.
    :param color: Color (pygame.Color | tuple): cor alvo do fade-in.
    :param duration: Duration (float): tempo total da animação em segundos.
    :param step: ‘Step’ (int): incremento da opacidade (quanto menor, mais suave).
    :param title: Title (str | None): texto opcional para exibir durante o fade-in.
    :param font: Pygame.Font | None: fonte opcional para renderizar o título.
    :param font_percent: Font_percent (int): tamanho da fonte em porcentagem da altura da tela.
    :param margin_top_percent: Margin_top_percent (int): margem superior em porcentagem da altura da tela.
    :return: Fade-in.
    """
    surf = window.get_surface()
    total_steps = int(255 / step)
    delay = duration / total_steps

    # fonte para título
    text_surface = None
    text_rect = None
    if title:
        if font is None:
            font_size = int(window.size[1] * (font_percent / 100))
            font = pygame.font.Font(None, font_size)

        text_surface = font.render(title, True, (255, 255, 255))

        # centralização horizontal
        text_rect = text_surface.get_rect()
        text_rect.centerx = window.size[0] // 2
        text_rect.top = int(window.size[1] * (margin_top_percent / 100))

    # fade_in
    for alpha in range(0, 256, step):
        fade_surface = pygame.Surface(window.size)
        fade_surface.fill(color)
        fade_surface.set_alpha(alpha)

        surf.fill("black")
        surf.blit(fade_surface, (0, 0))

        if title and text_surface:
            text_with_alpha = text_surface.copy()
            text_with_alpha.set_alpha(alpha)
            surf.blit(text_with_alpha, text_rect)

        window.flip()
        time.sleep(delay)

def breath_step(step, pixels=1, hold=2):
    """
    Calcula o deslocamento Y para animação de respiro.
    :param step: Contador de frames (int).
    :param pixels: Quantidade de pixels para deslocar.
    :param hold: Quantos frames cada etapa permanece (delay entre movimentos).
    :return: Deslocamento em Y (int).
    """
    sequence = [0, -pixels, -pixels, -pixels, 0, +pixels, +pixels, +pixels]
    index = (step // hold) % len(sequence)
    return sequence[index]