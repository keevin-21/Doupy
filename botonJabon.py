import pygame
from pygame import *
from constantes import SPRITE_BOTON_JABON, CENTRO_ALTO, CENTRO_ANCHO

pygame.init()

class BotonJabon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenBoton = SPRITE_BOTON_JABON.subsurface((0, 0), (64, 64))
        self.click = False
        self.imagen = self.imagenBoton
        self.imagen = pygame.transform.scale(self.imagen, (64 + 32, 64 + 32))
        self.ancho = CENTRO_ANCHO
        self.alto = CENTRO_ALTO - 200
        self.rect = self.imagen.get_rect()
        self.rect.topleft = self.ancho, self.alto

    def update(self):
        self.imagen = pygame.transform.scale(self.image, (64 + 32, 64 +32))