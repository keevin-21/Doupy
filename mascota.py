import pygame
from pygame.locals import *
from constantes import leerSpriteSheet, SPRITE_SHEET, SPRITE_ACARICIAR, SPRITE_COMER

pygame.init()

class Mascota(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Configurando los sprites para cada dirección
        self.imgEstatico = leerSpriteSheet(0, 3, SPRITE_SHEET, 120, 130)
        self.imgAbajo = leerSpriteSheet(3, 13, SPRITE_SHEET, 120, 130)
        self.imgIzquierda = leerSpriteSheet(13, 23, SPRITE_SHEET, 120, 130)
        self.imgArriba = leerSpriteSheet(23, 33, SPRITE_SHEET, 120, 130)
        self.imgDerecha = leerSpriteSheet(33, 43, SPRITE_SHEET, 120, 130)
        self.imgAcariciar = leerSpriteSheet(0, 3, SPRITE_ACARICIAR, 120, 130)
        self.imgComer = leerSpriteSheet(0, 3, SPRITE_COMER, 120, 130)
        self.accion = 0  # 0: estático 1: abajo 2: izquierda 3: arriba 4: derecha 5: acariciar, 6: comer
        self.indiceFrame = 0
        self.imagen = self.imgEstatico[self.indiceFrame]
        self.imagen = pygame.transform.scale(self.imagen, (120, 130))
        self.mascara = pygame.mask.from_surface(self.imagen)

        # Configurando la variable de control de movimiento
        self.temporizadorAndar = pygame.USEREVENT + 1
        pygame.time.set_timer(self.temporizadorAndar, 5000)

        # Configurando el rect del sprite y generando la posición inicial
        self.nuevoX = 300
        self.nuevoY = 300
        self.x = 300
        self.y = 300
        self.rect = self.imagen.get_rect()
        self.rect.topleft = self.x, self.y

        # Variables de control
        self.acariciado = False
        self.comiendo = False

        # Parámetros de vida
        self.hambre = 150.00
        self.limpieza = 150.00
        self.felicidad = (self.hambre + self.limpieza) // 2

        self.bajarHambre = pygame.USEREVENT + 4
        pygame.time.set_timer(self.bajarHambre, 5000)

        self.bajarLimpieza = pygame.USEREVENT + 5
        pygame.time.set_timer(self.bajarLimpieza, 5000)

    def update(self):
        if self.nuevoX != self.rect.x:
            if self.nuevoX > self.rect.x:
                self.actualizarAccion(4)
                if (self.rect.x + 2) > self.nuevoX:
                    self.nuevoX = self.rect.x
                if self.nuevoX == self.rect.x and self.nuevoY != self.rect.y:
                    if self.nuevoY > self.rect.y:
                        self.actualizarAccion(1)
                    elif self.nuevoY < self.rect.y:
                        self.actualizarAccion(3)

            if self.nuevoX < self.rect.x:
                self.actualizarAccion(2)
                if (self.rect.x - 2) < self.nuevoX:
                    self.nuevoX = self.rect.x
                if self.nuevoX == self.rect.x and self.nuevoY != self.rect.y:
                    if self.nuevoY > self.rect.y:
                        self.actualizarAccion(1)
                    elif self.nuevoY < self.rect.y:
                        self.actualizarAccion(3)

            if self.nuevoY < self.rect.y and self.nuevoX < self.rect.x + 240 and self.nuevoX > self.rect.x - 120:
                self.actualizarAccion(3)
                if (self.rect.y - 2) < self.nuevoY:
                    self.nuevoY = self.rect.y
                if self.nuevoY == self.rect.y and self.nuevoX != self.rect.x:
                    if self.nuevoX > self.rect.x:
                        self.actualizarAccion(4)
                    elif self.nuevoX < self.rect.x:
                        self.actualizarAccion(2)

            if self.nuevoY > self.rect.y and self.nuevoX < self.rect.x + 240 and self.nuevoX > self.rect.x - 120:
                self.actualizarAccion(1)
                if (self.rect.y + 2) < self.nuevoY:
                    self.nuevoY = self.rect.y
                if self.nuevoY == self.rect.y and self.nuevoX != self.rect.x:
                    if self.nuevoX > self.rect.x:
                        self.actualizarAccion(4)
                    elif self.nuevoX < self.rect.x:
                        self.actualizarAccion(2)

        if self.nuevoX == self.rect.x and self.nuevoY == self.rect.y and not self.colisionRaton():
            if self.comiendo:
                self.actualizarAccion(6)
            else:
                self.actualizarAccion(0)

        if self.accion == 0:
            self.imagen = self.imgEstatico[int(self.indiceFrame)]
            self.indiceFrame += 0.05
            if self.indiceFrame >= len(self.imgEstatico):
                self.indiceFrame = 0

        elif self.accion == 1:
            self.imagen = self.imgAbajo[int(self.indiceFrame)]
            self.indiceFrame += 0.2
            self.rect.y += 2
            if self.indiceFrame >= len(self.imgAbajo):
                self.indiceFrame = 0
                self.actualizarAccion(0)

        elif self.accion == 2:
            self.imagen = self.imgIzquierda[int(self.indiceFrame)]
            self.indiceFrame += 0.2
            self.rect.x -= 2
            if self.nuevoY < self.rect.y:
                self.rect.y -= 2
            if self.nuevoY > self.rect.y:
                self.rect.y += 2
            if self.indiceFrame >= len(self.imgIzquierda):
                self.indiceFrame = 0
                self.actualizarAccion(0)

        elif self.accion == 3:
            self.imagen = self.imgArriba[int(self.indiceFrame)]
            self.indiceFrame += 0.5
            self.rect.y -= 2
            if self.indiceFrame >= len(self.imgArriba):
                self.indiceFrame = 0
                self.actualizarAccion(0)

        elif self.accion == 4:
            self.imagen = self.imgDerecha[int(self.indiceFrame)]
            self.indiceFrame += 0.2
            self.rect.x += 2
            if self.nuevoY < self.rect.y:
                self.rect.y -= 2
            if self.nuevoY > self.rect.y:
                self.rect.y += 2
            if self.indiceFrame >= len(self.imgDerecha):
                self.indiceFrame = 0

        elif self.accion == 5:
            self.imagen = self.imgAcariciar[int(self.indiceFrame)]
            self.indiceFrame += 0.05
            if self.indiceFrame >= len(self.imgAcariciar):
                self.indiceFrame = 0
                self.actualizarAccion(0)

        elif self.accion == 6:
            self.imagen = self.imgComer[int(self.indiceFrame)]
            self.indiceFrame += 0.05
            if self.indiceFrame >= len(self.imgComer):
                self.indiceFrame = 0

        self.imagen = pygame.transform.scale(self.imagen, (120, 130))
        self.felicidad = (self.hambre + self.limpieza) // 2

    def actualizarAccion(self, nuevaAccion):
        if nuevaAccion != self.accion:
            self.accion = nuevaAccion
            self.indiceFrame = 0

    def colisionRaton(self):
        return self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]
