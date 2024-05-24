import pygame
from pygame.locals import *
from datetime import datetime
from sys import exit
from constantes import ANCHO_PANTALLA, ALTO_PANTALLA, BACKGROUND, RELOJ_JUEGO
from constantes import grupoSprites
from mascota import Doupy
from botonComida import BotonComida
from botonJabon import BotonJabon
from comida import Comida
from jabon import Jabon
from barra import Barras
from mouse import Mouse
from random import randint


pygame.init()
clock = RELOJ_JUEGO

pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.load("soundtrack/BGM.mp3")
pygame.mixer.music.play(-1)

# Set up display
BACKGROUND = pygame.transform.scale(BACKGROUND, (ANCHO_PANTALLA, ALTO_PANTALLA))
ventana = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Doupy")

mascota = Doupy()
botonComida = BotonComida()
botonJabon = BotonJabon()
barraComida = Barras(mascota.comer, 30, 20)
barraLimpieza = Barras(mascota.limpio, 30, 50)
barraFelicidad = Barras(mascota.felicidad, 30, 80)
mouse = Mouse(pygame.mouse.get_pos())
todosLosSprites = grupoSprites(mascota, botonComida, botonJabon, barraComida, barraLimpieza, barraFelicidad, mouse)
pararComida = False
jabonExiste = False
comidaExiste = False
grupoComida = pygame.sprite.Group()
grupoJabon = pygame.sprite.Group()


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
