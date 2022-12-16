import pygame


def final(window):
    texto_final = pygame.font.Font('freesansbold.ttf', 70)
    text = texto_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    window.blit(text, (60, 200))
