import pygame


def title():
    return pygame.display.set_caption('Invasión espacial')


def icon():
    icon_window = pygame.image.load('img/ovni.png')
    return pygame.display.set_icon(icon_window)


def background_screen():
    # background = (209,144,228)
    # screen.fill(background)
    background = pygame.image.load('img/Fondo.jpg')
    return background
