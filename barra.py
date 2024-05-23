import pygame
from constantes import leerSpriteSheet, SPRITE_BARRA

pygame.init()

class Barras(pygame.sprite.Sprite):
    def __init__(self, parametro, posicionAlto, posicionAncho):
        pygame.sprite.Sprite.__init__(self)
        self.imagenBarra = leerSpriteSheet(0, 15, SPRITE_BARRA, 60, 20)
        self.estadoActual = parametro
        self.indexFrame = 0
        self.imagen = self.imagenBarra[self.indexFrame]
        self.imagen = pygame.transform.scale(self.imagen, (60, 20))
        self.alto = posicionAlto
        self.ancho = posicionAncho
        self.rect = self.imagen.get_rect()
        self.rect.topleft = self.alto, self.ancho
    
    def update(self):
        self.imagen = self.imagenBarra[self.indexFrame]

    def decrecerBarra(self, estado):
        if estado (self.estadoActual - 10) and self.indexFrame < 15:
            self.indexFrame += 1
            self.estadoActual = estado

    def crecerBarra(self, estado):
        if estado == (self.estadoActual + 10) and self.indexFrame > 0:
            self.indexFrame -= 1
            self.estadoActual = estado