import pygame


class Bala:
    bala = pygame.image.load('img/bala.png')
    bala_pos_x = 0
    bala_pos_y = 500
    change_bala_pos_x = 0
    velocidad_bala = 10
    visible = False

    @classmethod
    def pos_bala(cls, x, y, screen):
        cls.visible = True
        cls.bala_pos_x = x
        # bala aparece en el centro de la nave
        return screen.blit(cls.bala, (cls.bala_pos_x + 16, y + 10))

    @classmethod
    def mov_bala(cls, y, screen):
        if cls.bala_pos_y <= -64:
            cls.bala_pos_y = 500
            cls.visible = False

        if cls.visible:
            cls.pos_bala(cls.bala_pos_x, y, screen)
            cls.bala_pos_y -= cls.velocidad_bala

