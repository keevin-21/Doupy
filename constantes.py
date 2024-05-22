import pygame
from pygame.locals import *
import os

def leerSpriteSheet(iniciarCortar, finalCortar, spriteSheet, anchoSprite, altoSprite):
    imagenes = []
    for i in range(iniciarCortar, finalCortar):
        imagen = spriteSheet.subsurface((i * anchoSprite, 0), (anchoSprite, altoSprite))
        imagenes.append(imagen)

    return imagenes

def grupoSprites(*sprites):
    grupo = pygame.sprite.Group()
    for sprite in sprites:
        grupo.add(sprite)

    return grupo

# Pantalla
ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480
CENTRO_ANCHO = 640 / 2
CENTRO_ALTO = 480 / 2

# Fuente
FUENTE = pygame.font.SysFont("comicsansms", 35, True, False)

# Reloj
RELOJ_JUEGO = pygame.time.Clock()

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Directorios
DIRECTORIO_PRINCIPAL = os.path.dirname(__file__)
DIRECTORIO_IMAGENES = os.path.dirname(DIRECTORIO_PRINCIPAL, "sprites")
DIRECTORIO_MUSICA = os.path.dirname(DIRECTORIO_PRINCIPAL, "soundtrack")
# no existe ^^^

# Sprites
SPRITE_BOTON_COMIDA = pygame.image.load(os.path.join(DIRECTORIO_PRINCIPAL, "apple_button.png"))
SPRITE_BOTON_JABON = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, "soap_button.png"))