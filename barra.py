import pygame
from pygame.locals import *
from constantes import leerSpriteSheet, SPRITE_BARRA

pygame.init()

class Barras(pygame.sprite.Sprite):

    def __init__(self, parametro, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.imgBarra = leerSpriteSheet(0, 15, SPRITE_BARRA, 60, 20)
        self.estadoActual = parametro
        self.indexFrame = 0
        self.image = self.imgBarra[self.indexFrame]
        self.image = pygame.transform.scale(self.image, (60, 20))
        self.x = posX
        self.y = posY
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

    def update(self):
        self.image = self.imgBarra[int(self.indexFrame)]
        self.image = pygame.transform.scale(self.image, (60, 20))

    def bajarBarra(self, estado):
        if estado == (self.estadoActual - 10) and self.indexFrame < 15:
            self.indexFrame += 1
            self.estadoActual = estado

    def subirBarra(self, estado):
        if estado == (self.estadoActual + 10) and self.indexFrame > 0:
            self.indexFrame -= 1
            self.estadoActual = estado
