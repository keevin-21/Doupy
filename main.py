import pygame
from mascota import Mascota
from constantes import ANCHO_PANTALLA, ALTO_PANTALLA, BACKGROUND, grupoSprites 
from barra import Barras

pygame.init()

# se inicializa la musica
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.load("soundtrack/BGM.mp3")
pygame.mixer.music.play(-1)

BACKGROUND = pygame.transform.scale(BACKGROUND, (ANCHO_PANTALLA, ALTO_PANTALLA))

ventana = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Doupy")