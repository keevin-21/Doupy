import pygame
import random

def pong_game():
    pygame.init()

    pygame.display.set_caption("Link Pong")


    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    WIDTH = 800
    HEIGHT = 600
    size = (WIDTH, HEIGHT)
    player_width = 15
    player_height = 90

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    #coordenadas y velocidad de jugador 1
    player1_x_coor = 50
    player1_y_coor = HEIGHT / 2 - player_height / 2
    player1_y_speed = 0

    #coordenadas y velocidad de jugador 2 (IA)
    player2_x_coor = WIDTH - 50 - player_width
    player2_y_coor = HEIGHT / 2 - player_height / 2
    player2_y_speed = 0
    ai_speed = 5

    # coordenadas de la pelota
    pelota_x = WIDTH / 2
    pelota_y = HEIGHT / 2
    pelota_speed_x = 9 * random.choice((-1, 1))
    pelota_speed_y = 9 * random.choice((-1, 1))

    score_player = 0
    score_machine = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # Movimiento del jugador
            if event.type == pygame.KEYDOWN:
                # jugador 1
                if event.key == pygame.K_w:
                    player1_y_speed = -9
                if event.key == pygame.K_s:
                    player1_y_speed = 9
                    

            if event.type == pygame.KEYUP:
                # jugador 1
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player1_y_speed = 0
                    
        
        if player1_y_coor < 0:
            player1_y_coor = size[1] -10
        if player1_y_coor > HEIGHT:
            player1_y_coor = 0
        

        # Movimiento de la IA
        if pelota_x > WIDTH / 2:  # Solo mueve la IA si la pelota está en su lado
            if pelota_y < player2_y_coor + player_height / 2:
                player2_y_speed = -ai_speed
            elif pelota_y > player2_y_coor + player_height / 2:
                player2_y_speed = ai_speed
            else:
                player2_y_speed = 0
        else:
            player2_y_speed = 0

        #revisa si la pelota sale de la pantalla
        if pelota_y > HEIGHT - 10 or pelota_y < 10:
            pelota_speed_y *= -1

        #revisa si la pelota sale del lado derecho
        if pelota_x > WIDTH:
            score_player += 1
            pelota_x = WIDTH / 2
            pelota_y = HEIGHT / 2
            pelota_speed_x = 9 * random.choice((-1, 1))
            pelota_speed_y = 9 * random.choice((-1, 1))
        elif pelota_x < 0:
            score_machine += 1
            pelota_x = WIDTH / 2
            pelota_y = HEIGHT / 2
            pelota_speed_x = 9 * random.choice((-1, 1))
            pelota_speed_y = 9 * random.choice((-1, 1))

        # modificar coordenadas para dar movimiento a los jugadores/pelota
        player1_y_coor += player1_y_speed
        player2_y_coor += player2_y_speed
        #movimiento pelota
        pelota_x += pelota_speed_x
        pelota_y += pelota_speed_y

        screen.fill(black)
        # ZONA DE DIBUJO
        jugador1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor, player_width, player_height))
        jugador2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor, player_width, player_height))
        pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)

        #colisiones
        if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
            pelota_speed_x *= -1

        # ZONA DE DIBUJO
        
        def draw_score():
            font = pygame.font.Font(None, 74)
            score = "{} - {}".format(score_player, score_machine)
            text = font.render(score, True, white)
            screen.blit(text, (WIDTH / 2 - text.get_width() / 2, 10))

            if score_player == 5:
                win_text = font.render("Ganaste!", True, white)
                screen.blit(win_text, (WIDTH / 2 - win_text.get_width() / 2, HEIGHT / 2))
                pygame.display.flip()
                pygame.time.delay(3000)  
                game_over = True
                # pygame.quit()  
            elif score_machine == 5:
                lose_text = font.render("Perdiste!", True, white)
                screen.blit(lose_text, (WIDTH / 2 - lose_text.get_width() / 2, HEIGHT / 2))
                pygame.display.flip()
                pygame.time.delay(3000) 
                game_over = True 
                # pygame.quit()  
        draw_score()
        pygame.display.flip()
        clock.tick(60)

    # pygame.quit()

