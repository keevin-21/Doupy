import pygame
from pygame.locals import *
from constantes import leerSpriteSheet, SPRITE_SHEET, SPRITE_ACARICIAR, SPRITE_COMER


pygame.init()


class Mascota(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # setando os sprites de cada direção
        self.img_stoped = leerSpriteSheet(0, 3, SPRITE_SHEET, 120, 130)
        self.img_down = leerSpriteSheet(3, 13, SPRITE_SHEET, 120, 130)
        self.img_left = leerSpriteSheet(13, 23, SPRITE_SHEET, 120, 130)
        self.img_up = leerSpriteSheet(23, 33, SPRITE_SHEET, 120, 130)
        self.img_right = leerSpriteSheet(33, 43, SPRITE_SHEET, 120, 130)
        self.img_afago = leerSpriteSheet(0, 3, SPRITE_ACARICIAR, 120, 130)
        self.img_comer = leerSpriteSheet(0, 3, SPRITE_COMER, 120, 130)
        self.action = 0
        self.indexFrame = 0
        self.image = self.img_stoped[self.indexFrame]
        self.image = pygame.transform.scale(self.image, (120, 130))
        self.mask = pygame.mask.from_surface(self.image)
        
        self.temporizadorAndar = pygame.USEREVENT + 1
        pygame.time.set_timer(self.temporizadorAndar, 300)

        self.newx = 200
        self.newy = 100
        self.x = 200
        self.y = 100
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

        self.afagado = False
        self.comendo = False

        self.hambre = 150.00
        self.limpieza = 150.00
        self.felicidad = (self.hambre + self.limpieza)//2

        self.bajarHambre = pygame.USEREVENT + 4
        pygame.time.set_timer(self.bajarHambre, 300)

        self.bajarLimpieza = pygame.USEREVENT + 5
        pygame.time.set_timer(self.bajarLimpieza, 300)

    def update(self):

        if self.newx != self.rect.x:
            if isinstance(self.rect.x, int) and self.nuevoX > self.rect.x:
                self.actualizarAccion(4)
                if (self.rect.x + 2) > self.newx:
                    self.newx = self.rect.x
                if self.newx == self.rect.x and self.newy != self.rect.y:
                    if self.newy > self.rect.y:
                        self.actualizarAccion(1)
                    elif self.newy < self.rect.y:
                        self.actualizarAccion(3)

            if self.newx < self.rect.x:
                self.actualizarAccion(2)
                if (self.rect.x - 2) < self.newx:
                    self.newx = self.rect.x
                if self.newx == self.rect.x and self.newy != self.rect.y:
                    if self.newy > self.rect.y:
                        self.actualizarAccion(1)
                    elif self.newy < self.rect.y:
                        self.actualizarAccion(3)

            if self.newy < self.rect.y and self.newx < self.rect.x + 240 and self.newx > self.rect.x - 120:
                self.actualizarAccion(3)
                if (self.rect.y - 2) < self.newy:
                    self.newy = self.rect.y
                if self.newy == self.rect.y and self.newx != self.rect.x:
                    if self.newx > self.rect.x:
                        self.actualizarAccion(4)
                    elif self.newx < self.rect.x:
                        self.actualizarAccion(2)

            if self.newy > self.rect.y and self.newx < self.rect.x + 240 and self.newx > self.rect.x - 120:
                self.actualizarAccion(1)
                if (self.rect.y + 2) < self.newy:
                    self.newy = self.rect.y
                if self.newy == self.rect.y and self.newx != self.rect.x:
                    if self.newx > self.rect.x:
                        self.actualizarAccion(4)
                    elif self.newx < self.rect.x:
                        self.actualizarAccion(2)


        if self.newx == self.rect.x and self.newy == self.rect.y and self.mouse_colidindo() == False:
            if self.comendo == True:
                self.actualizarAccion(6)

            else:
                self.actualizarAccion(0)

        if self.action == 0:
            self.image = self.img_stoped[int(self.indexFrame)]
            self.indexFrame += 0.05
            if self.indexFrame >= len(self.img_stoped):
                self.indexFrame = 0

        elif self.action == 1:
            self.image = self.img_down[int(self.indexFrame)]
            self.indexFrame += 0.2
            self.rect.y += 2
            if self.indexFrame >= len(self.img_down):
                self.indexFrame = 0
                self.actualizarAccion(0)

        elif self.action == 2:
            self.image = self.img_left[int(self.indexFrame)]
            self.indexFrame += 0.2
            self.rect.x -= 2
            if self.newy < self.rect.y:
                self.rect.y -= 2
            if self.newy > self.rect.y:
                self.rect.y += 2
            if self.indexFrame >= len(self.img_left):
                self.indexFrame = 0
                self.actualizarAccion(0)

        elif self.action == 3:
            self.image = self.img_up[int(self.indexFrame)]
            self.indexFrame += 0.5
            self.rect.y -= 2
            if self.indexFrame >= len(self.img_up):
                self.indexFrame = 0
                self.actualizarAccion(0)

        elif self.action == 4:
            self.image = self.img_right[int(self.indexFrame)]
            self.indexFrame += 0.2
            self.rect.x += 2
            if self.newy < self.rect.y:
                self.rect.y -= 2
            if self.newy > self.rect.y:
                self.rect.y += 2
            if self.indexFrame >= len(self.img_right):
                self.indexFrame = 0

        elif self.action == 5:
            # pygame.time.set_timer(self.temporizadorAndar, 0)
            self.image = self.img_afago[int(self.indexFrame)]
            self.indexFrame += 0.05
            if self.indexFrame >= len(self.img_afago):
                self.indexFrame = 0
                self.actualizarAccion(0)

        elif self.action == 6:
            # pygame.time.set_timer(self.temporizadorAndar, 0)
            self.image = self.img_comer[int(self.indexFrame)]
            self.indexFrame += 0.05
            if self.indexFrame >= len(self.img_comer):
                self.indexFrame = 0

        self.image = pygame.transform.scale(self.image, (240, 260))
        self.felicidad = (self.hambre + self.limpieza)//2

    def actualizarAccion(self, new_action):
        # print(new_action, self.action)
        if new_action != self.action:
            self.action = new_action
            self.indexFrame = 0

    def mouse_colidindo(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) == True and pygame.mouse.get_pressed()[0] == True:
            return True
        else:
            return False
