import pygame
from constantes import ANCHO_PANTALLA, ALTO_PANTALLA, BACKGROUND, RELOJ_JUEGO

pygame.init()
clock = RELOJ_JUEGO

pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.load("soundtrack/BGM.mp3")
pygame.mixer.music.play(-1)

# Set up display
BACKGROUND = pygame.transform.scale(BACKGROUND, (ANCHO_PANTALLA, ALTO_PANTALLA))
ventana = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Doupy")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ventana.blit(BACKGROUND, (0, 0))
    pygame.display.update()

    clock.tick(60)

pygame.quit()
