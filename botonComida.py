import pygame
from pygame.locals import *
from constantes import SPRITE_BOTON_COMIDA

pygame.init()

class BotonComida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgBoton = SPRITE_BOTON_COMIDA.subsurface((0, 0), (64, 64))
        self.botonClicado = False
        self.imagen = self.imgBoton
        self.imagen = pygame.transform.scale(self.imagen, (64 + 32, 64 + 32))
        self.x = 112
        self.y = 374
        self.rect = self.imagen.get_rect()
        self.rect.topleft = self.x, self.y

    def update(self):
        self.imagen = pygame.transform.scale(self.imagen, (64 + 32, 64 + 32))
