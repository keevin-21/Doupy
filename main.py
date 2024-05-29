import pygame
from pygame.locals import *
from sys import exit
from random import randint
from datetime import datetime
from mascota import Mascota
from barra import Barras
from botonComida import BotonComida
from botonJabon import BotonJabon
from comida import Comida
from jabon import Jabon
from constantes import recuperarProgreso, leerSpriteSheet, BACKGROUND, ALTO_PANTALLA, ANCHO_PANTALLA, RELOJ_JUEGO, NEGRO, FUENTE_CS, POSICION_RELOJ

pygame.init()

pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.load("soundtrack/BGM.mp3")
pygame.mixer.music.play(-1)

BACKGROUND = pygame.transform.scale(BACKGROUND, (ANCHO_PANTALLA, ALTO_PANTALLA))
ventana = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("DOUPY")

mascota = Mascota()
mascota.hambre, mascota.limpieza = recuperarProgreso(mascota.hambre, mascota.limpieza)
