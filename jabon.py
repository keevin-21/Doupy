import pygame
from pygame.locals import *
from constantes import leer_sprites, SPRITE_JABON

pygame.init()

class Jabon(pygame.sprite.Sprite):

    def __init__(self, mousePos):
        pygame.sprite.Sprite.__init__(self)
        self.usandoJabon = leer_sprites(0, 5, SPRITE_JABON, 64, 64)
        self.indexFrame = 0
        self.image = self.usandoJabon[self.indexFrame]
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.suelto = False
        self.usando = False
        self.desaparecer = pygame.USEREVENT + 3
        pygame.time.set_timer(self.desaparecer, 0)
        self.x, self.y = mousePos
        self.x -= 32
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

    def update(self):
        if self.suelto == False:
            if pygame.mouse.get_pressed()[0] == True:
                self.rect.x, self.rect.y = pygame.mouse.get_pos()
                self.rect.x -= 32
                if self.usando == True:
                    self.image = self.usandoJabon[int(self.indexFrame)]
                    self.indexFrame += 0.1
                    if self.indexFrame >= len(self.usandoJabon):
                        self.indexFrame = 0
                else:
                    self.indexFrame = 0
            else:
                pygame.time.set_timer(self.desaparecer, 100)
                self.suelto = True

        self.image = pygame.transform.scale(self.image, (64 + 32, 64 + 32))
