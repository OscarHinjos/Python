import pygame
from random import *
from dia10.Services.final_juego import *

class Enemigo:
    enemigo = pygame.image.load('img/enemigo.png')

    change_enemigo_pos_x = 2.5
    change_enemigo_pos_y = 50

    def __init__(self, x, y):
        self.enemigo_pos_x = x
        self.enemigo_pos_y = y

    def pos_enemigo(self, screen):
        return screen.blit(self.enemigo, (self.enemigo_pos_x, self.enemigo_pos_y))

    def move_enemigo(self):

        self.enemigo_pos_x += self.change_enemigo_pos_x

    def limite_enemigo(self):
        if self.enemigo_pos_x <= 0:
            self.change_enemigo_pos_x = 2.5
            self.enemigo_pos_y += self.change_enemigo_pos_y
        elif self.enemigo_pos_x >= 736:
            self.change_enemigo_pos_x = -2.5
            self.enemigo_pos_y += self.change_enemigo_pos_y

    def muerte(self):
        self.enemigo_pos_x = 0
        self.enemigo_pos_y = 0
