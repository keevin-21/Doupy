import pygame
import random

def pong_game():
    pygame.init()

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    HEIGHT = 800
    WIDTH = 600
    size = (HEIGHT, WIDTH)
    player_width = 15
    player_height = 90

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    #coordenadas y velocidad de jugador 1
    player1_x_coor = 50
    player1_y_coor = 300 - 45
    player1_y_speed = 0

    #coordenadas y velocidad de jugador 2 (IA)
    player2_x_coor = 750 - player_width
    player2_y_coor = 300 - 45
    player2_y_speed = 0
    ai_speed = 10

    # coordenadas de la pelota
    pelota_x = 400
    pelota_y = 300
    pelota_speed_x = 10
    pelota_speed_y = 10

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # Movimiento del jugador
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # jugador 1
                if event.key == pygame.K_w:
                    player1_y_speed = -10
                if event.key == pygame.K_s:
                    player1_y_speed = 10


            if event.type == pygame.KEYUP:
                # jugador 1
                if event.key == pygame.K_w:
                    player1_y_speed = 0
                if event.key == pygame.K_s:
                    player1_y_speed = 0
                     

        # Movimiento de la IA
        if pelota_x > size[0] / 2:  # Solo mueve la IA si la pelota está en su lado
            if pelota_y < player2_y_coor + player_height / 2:
                player2_y_speed = -ai_speed
            elif pelota_y > player2_y_coor + player_height / 2:
                player2_y_speed = ai_speed
            else:
                player2_y_speed = 0
        else:
            player2_y_speed = 0

        if pelota_y > size[1] - 10 or pelota_y < 10:
            pelota_speed_y *= -1
        
        #revisa si el jugador1 sale de la pantalla
        if player1_y_coor < 0:
            player1_y_coor = size[1] - 10

        if player1_y_coor > size[1] - 5:
            player1_y_coor = 0

        #revisa si el jugador2 sale de la pantalla
        if player2_y_coor < 0:
            player2_y_coor = size[1] - 20

        if player2_y_coor > size[1] - 5:
            player2_y_coor = 0

        #revisa si la pelota sale del lado derecho
        if pelota_x > size[0] or pelota_x < 0:
            pelota_y = 300
            pelota_x = 400
            
            #si la pelota sale de la pantalla, se invierte la velocidad
            pelota_speed_x *= -1
            pelota_speed_y *= -1

        # modificar coordenadas para dar movimiento a los jugadores/pelota
        player1_y_coor += player1_y_speed
        player2_y_coor += player2_y_speed
        #movimiento pelota
        pelota_x += pelota_speed_x
        pelota_y += pelota_speed_y

        screen.fill(black)
        # ZONA DE DIBUJO
        jugador1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor - 45, player_width, player_height))
        jugador2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor - 45, player_width, player_height))
        pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)

        #colisiones
        if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
            pelota_speed_x *= -1

        # ZONA DE DIBUJO
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

pong_game()