import pygame
from constantes import leerSpriteSheet, SPRITE_BARRA

pygame.init()

class Barras(pygame.sprite.Sprite):
    def __init__(self, parametro, posicionAlto, posicionAncho):
        super().__init__()
        self.imagenBarra = leerSpriteSheet(0, 15, SPRITE_BARRA, 60, 20)
        self.estadoActual = parametro
        self.indexFrame = 0
        self.image = self.imagenBarra[self.indexFrame]
        self.image = pygame.transform.scale(self.image, (60, 20))
        self.rect = self.image.get_rect()
        self.rect.topleft = posicionAlto, posicionAncho
    
    def update(self):
        self.image = self.imagenBarra[self.indexFrame]

    def decrecerBarra(self, estado):
        if estado < self.estadoActual and self.indexFrame < 15:
            self.indexFrame += 1
            self.estadoActual = estado

    def crecerBarra(self, estado):
        if estado > self.estadoActual and self.indexFrame > 0:
            self.indexFrame -= 1
            self.estadoActual = estado
