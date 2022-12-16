import time
from pygame import *
from dia10.Services.title_icon_color import *
from dia10.Services.protagonist import *
from dia10.Services.enemigo import *
from dia10.Services.bala import *
from dia10.Services.colision import *
from dia10.Services.llamar_enemigos import *
from dia10.Services.final_juego import *

"""
Inicializar pygame
"""
pygame.init()


def screen():
    # Variable pantalla
    window_size = (800, 600)
    window = pygame.display.set_mode(window_size)
    execute = False
    # Funciones titulo e icono
    title()
    icon()
    # puntuacion
    puntuacion = 0

    def ver_puntuacion(x, y):
        texto = fuente.render(f"Puntos: {puntuacion}", True, (255, 255, 255))
        window.blit(texto, (x, y))

    fuente = pygame.font.Font('freesansbold.ttf', 32)
    texto_x = 10
    texto_y = 10
    # Lista enemigos
    list_enemigo = list_enemigos()
    # musica
    mixer.music.load('music/MusicaFondo.mp3')
    mixer.music.play(-1)
    while not execute:
        window.blit(background_screen(), (0, 0))
        # bucles para eventos
        for event in pygame.event.get():
            """
            Cerrar pantalla
            """
            if event.type == pygame.QUIT:
                execute = True
            """
            Mover player
            """
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Player.change_player_pos_x = -3
                if event.key == pygame.K_RIGHT:
                    Player.change_player_pos_x = 3
                if event.key == pygame.K_SPACE:
                    mixer.Sound('music/disparo.mp3').play()
                    if not Bala.visible:
                        Bala.pos_bala(Player.player_pos_x, Player.player_pos_y, window)
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or
                        event.key == pygame.K_RIGHT):
                    Player.change_player_pos_x = 0

        # Funciones Jugador
        Player.move_player()
        Player.limite_jugador()
        Player.pos_player(window)
        # Funciones Enemigo
        for enemigo in list_enemigo:
            enemigo.pos_enemigo(window)
            enemigo.move_enemigo()
            enemigo.limite_enemigo()
            # Colision
            colisiones = colision(enemigo.enemigo_pos_x, enemigo.enemigo_pos_y, Bala.bala_pos_x, Bala.bala_pos_y)

            # Detectar colision
            if colisiones:
                mixer.Sound('music/Golpe.mp3').play()
                Bala.bala_pos_y = 500
                Bala.visible = False
                puntuacion += 1
                enemigo.muerte()

            if enemigo.enemigo_pos_y > 500:
               for en in list_enemigo:
                en.enemigo_pos_y = 1000
                final(window)

        # Movimiento bala
        Bala.mov_bala(Bala.bala_pos_y, window)
        ver_puntuacion(texto_x,texto_y)
        pygame.display.update()
