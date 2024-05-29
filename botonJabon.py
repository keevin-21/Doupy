import pygame
from pygame.locals import *
from constantes import SPRITE_BOTON_JABON

pygame.init()

class BotonJabon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgBoton = SPRITE_BOTON_JABON.subsurface((0, 0), (64, 64))
        self.botonClicado = False
        self.imagen = self.imgBoton
        self.imagen = pygame.transform.scale(self.imagen, (64 + 32, 64 + 32))
        self.x = 432
        self.y = 374
        self.rect = self.imagen.get_rect()
        self.rect.topleft = self.x, self.y

    def update(self):
        self.imagen = pygame.transform.scale(self.imagen, (64 + 32, 64 + 32))
