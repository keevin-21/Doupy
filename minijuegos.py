import pygame
import sys
from pong import pong_game
from minigame_dragons import minigame_dragons

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Minijuegos")

fondo = pygame.image.load("images/fondo-minijuegos.png")

# Definir colores
GOLD = (255, 223, 0)

# Definir rectángulos para los botones
button_1 = pygame.Rect(150, 200, 200, 100)
button_2 = pygame.Rect(450, 200, 200, 100)
button_minijuegos = pygame.Rect(300, 400, 100, 100) 

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    textrect.bottomright = (x, y)
    surface.blit(textobj, textrect)

def draw_start_screen():
    screen.blit(fondo, (0, 0))
    pygame.draw.rect(screen,GOLD , button_1)
    pygame.draw.rect(screen, GOLD, button_2)
    pygame.draw.rect(screen, GOLD, button_minijuegos)
    
    # Ajustar el tamaño de la fuente para que el texto se ajuste dentro de los botones
    font_size = 36
    font = pygame.font.Font(None, font_size)

    text1 = 'ping-pong 2players'
    text2 = 'sleeping dragons'
    text3 = 'minijuegos'
    # Reducir el tamaño de la fuente si el texto es más ancho que el botón
    while font.size(text1)[0] > button_1.width - 10:  # Un poco de margen
        font_size -= 1
        font = pygame.font.Font(None, font_size)
    
    draw_text(text1, font, (0, 0, 0), screen, button_1.centerx, button_1.centery)

    # Resetear el tamaño de la fuente para el segundo botón
    font_size = 36
    font = pygame.font.Font(None, font_size)

    while font.size(text2)[0] > button_2.width - 10:  # Un poco de margen
        font_size -= 1
        font = pygame.font.Font(None, font_size)

    draw_text(text2, font, (0, 0, 0), screen, button_2.centerx, button_2.centery)


    while font.size(text2)[0] > button_minijuegos.width - 10:  # Un poco de margen
        font_size -= 1
        font = pygame.font.Font(None, font_size)

    draw_text(text3, font, (0, 0, 0), screen, button_minijuegos.centerx, button_minijuegos.centery)

    pygame.display.flip()

def main():
    running = True
    while running:
        draw_start_screen()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(event.pos):
                    pong_game()
                    draw_start_screen()
                elif button_2.collidepoint(event.pos):
                    minigame_dragons()
                    draw_start_screen()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

# BOTON MINIJUEGOS
    # pygame.draw.rect(screen, GOLD, button_minijuegos)
    # while font.size(text2)[0] > button_2.width - 10:  # Un poco de margen
    #     font_size -= 1
    #     font = pygame.font.Font(None, font_size)

    # draw_text(text3, font, (0, 0, 0), screen, button_minijuegos.centerx, button_minijuegos.centery)
    
    # pygame.draw.rect(screen, GOLD, button_minijuegos)
