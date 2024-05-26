import pygame
from pygame.locals import *
from constantes import leerSpriteSheet, SPRITE_COMIDA

pygame.init()

class Comida(pygame.sprite.Sprite):
    def __init__(self, mousePos):
        pygame.sprite.Sprite.__init__(self)
        self.comidaEstatica = SPRITE_COMIDA.subsurface((0, 0), (32, 32))
        self.siendoComida = leerSpriteSheet(0, 5, SPRITE_COMIDA, 32, 32)
        self.indexFrame = 0
        self.imagen = pygame.transform.scale(self.comidaEstatica, (32 * 2, 32 * 2))
        self.empezarComida = False
        self.caido = False
        self.comidaTirada = False
        self.fueComido = False
        self.suelto = False
        self.sueltoPosicionY = None
        self.desaparecer = pygame.USEREVENT + 4
        pygame.time.set_timer(self.desaparecer, 0)  # temporizador inactivo
        self.x, self.y = mousePos
        self.rect = self.imagen.get_rect()
        self.rect.topleft = self.x, self.y

    def siendoComido(self):
        self.empezarComida = True

    def caer(self):
        self.caido = True

    def update(self):
        if self.empezarComida and not self.fueComido:
            self.imagen = self.siendoComida[int(self.indexFrame)]
            self.indexFrame += 0.005
            if self.indexFrame >= len(self.siendoComida):
                self.indexFrame = 5
                self.fueComido = True

        if self.caido and not self.fueComido:
            self.handle_caida()

        if not self.suelto:
            if pygame.mouse.get_pressed()[0]:
                self.rect.topleft = pygame.mouse.get_pos()
            else:
                self.sueltoPosicionY = self.rect.y
                self.caer()
                self.suelto = True

        self.imagen = pygame.transform.scale(self.imagen, (32 * 2, 32 * 2))

    def handle_caida(self):
        suelo = self.get_suelo_position(self.sueltoPosicionY)
        self.rect.y += 5
        if self.rect.y >= suelo:
            self.comidaTirada = True
            self.caido = False
            pygame.time.set_timer(self.desaparecer, 2000)  # desaparecer en 2 segundos

    def get_suelo_position(self, sueltoPosicionY):
        if sueltoPosicionY >= 300:
            return 400  # ajuste para un valor más realista
        elif sueltoPosicionY >= 200:
            return 380
        elif sueltoPosicionY >= 100:
            return 330
        else:
            return 290
        