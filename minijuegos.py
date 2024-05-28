import pygame
# import pgzrun
# import pgzero
import sys
from pong import pong_game
from minigame_dragons import minigame_dragons
# from game2 import game_2

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pantalla de Inicio")

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Definir rectángulos para los botones
button_1 = pygame.Rect(150, 200, 200, 100)
button_2 = pygame.Rect(450, 200, 200, 100)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def draw_start_screen():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, button_1)
    pygame.draw.rect(screen, RED, button_2)
    
    # Ajustar el tamaño de la fuente para que el texto se ajuste dentro de los botones
    font_size = 36
    font = pygame.font.Font(None, font_size)

    text1 = 'ping-pong 2players'
    text2 = 'sleeping dragons'

    # Reducir el tamaño de la fuente si el texto es más ancho que el botón
    while font.size(text1)[0] > button_1.width - 10:  # Un poco de margen
        font_size -= 1
        font = pygame.font.Font(None, font_size)
    
    draw_text(text1, font, WHITE, screen, button_1.centerx, button_1.centery)

    # Resetear el tamaño de la fuente para el segundo botón
    font_size = 36
    font = pygame.font.Font(None, font_size)

    while font.size(text2)[0] > button_2.width - 10:  # Un poco de margen
        font_size -= 1
        font = pygame.font.Font(None, font_size)

    draw_text(text2, font, WHITE, screen, button_2.centerx, button_2.centery)

    pygame.display.flip()

def main():
    running = True
    while running:
        draw_start_screen()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(event.pos):
                    pong_game()
                elif button_2.collidepoint(event.pos):
                    minigame_dragons()

if __name__ == "__main__":
    main()
