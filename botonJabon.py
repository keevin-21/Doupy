import pygame
from pygame.locals import *
from constantes import SPRITE_BOTON_JABON

pygame.init()

class BotonJabon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenBoton = SPRITE_BOTON_JABON.subsurface((0, 0), (64, 64))
        self.botonClicado = False
        self.image = self.imagenBoton
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.x = 432
        self.y = 374
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

    def actualizar(self):
        self.image = pygame.transform.scale(self.image, (64 + 32, 64 + 32))

