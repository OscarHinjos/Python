import pygame


class Player:
    player = pygame.image.load('img/cohete.png')
    player_pos_x = 368
    player_pos_y = 500
    change_player_pos_x = 0

    @classmethod
    def pos_player(cls, screen):
        return screen.blit(cls.player, (cls.player_pos_x, cls.player_pos_y))

    @classmethod
    def move_player(cls):
        cls.player_pos_x += cls.change_player_pos_x

    @classmethod
    def limite_jugador(cls):
        if cls.player_pos_x <= 0:
            cls.player_pos_x = 0
        elif cls.player_pos_x >= 736:
            cls.player_pos_x = 736
