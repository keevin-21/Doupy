import pygame
from pygame.locals import *
from constantes import SPRITE_BOTON_MINIJUEGOS

pygame.init()

class BotonMinijuegos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenBoton = SPRITE_BOTON_MINIJUEGOS.subsurface((0, 0), (64, 64))
        self.botonClicado = False
        self.image = self.imagenBoton
        self.image = pygame.transform.scale(self.image, (64 + 32, 64 + 32))
        self.x = 500
        self.y = 50
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

    def actualizar(self):
        self.image = pygame.transform.scale(self.image, (64 + 32, 64 + 32))
        
