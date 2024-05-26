import pygame
from constantes import leerSpriteSheet, SPRITE_LINK, SPRITE_COMER, SPRITE_ACARICIAR, CENTRO_ALTO, CENTRO_ANCHO

class Doupy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenDoupy = leerSpriteSheet(0, 3, SPRITE_LINK, 120, 130)
        self.imagenComer = leerSpriteSheet(0, 3, SPRITE_COMER, 120, 130)
        self.imagenAcariciar = leerSpriteSheet(0, 3, SPRITE_ACARICIAR, 120, 130)

        self.accion = 0 # 0 Doupy, 1 Comer, 2 Acariciar
        self.indexFrame = 0
        self.imagen = self.imagenDoupy[self.indexFrame]
        self. imagen = pygame.transform.scale(self.imagen, (120, 130))
        self.mascara = pygame.mask.from_surface(self.imagen)
        
        # evento de la animacion del sprite
        self.timerAnimacion = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timerAnimacion, 3000)

        # configurar la posicion inicial del sprite
        self.pocisionX = CENTRO_ANCHO
        self.posicionY = CENTRO_ALTO
        self.rect = self.imagen.get_rect()
        self.rect.topleft = self.pocisionX, self.posicionY

        # variables de control
        self.comer = False
        self.acariciar = False

        # valores en las variables de estado
        self.alimento = 200.00
        self.limpio = 200.00
        self.despierto = 200.00
        self.felicidad = (self.alimento + self.limpio + self.despierto) // 3
        
        self.decrementarAlimentacion = pygame.USEREVENT + 2
        pygame.time.set_timer(self.decrementarAlimentacion, 5000)

        self.decrementarLimpieza = pygame.USEREVENT + 3
        pygame.time.set_timer(self.decrementarLimpieza, 5000)

    # actualizar la animacion del sprite
    def update(self):
        if self.accion == 0:
            self.imagen = self.imagenDoupy[self.indexFrame]
        elif self.accion == 1:
            self.imagen = self.imagenComer[self.indexFrame]
        elif self.accion == 2:
            self.imagen = self.imagenAcariciar[self.indexFrame]

        self.imagen = pygame.transform.scale(self.imagen, (120, 130))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = self.pocisionX, self.posicionY
        self.felicidad = (self.alimento + self.limpio + self.despierto) // 3
    
    def updateAction(self, nuevaAccion):
        self.accion = nuevaAccion
        self.indexFrame = 0
    
    # detecta el el mouse esta colisionando con el sprite
    def colisionMouse(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) == True and pygame.mouse.get_pressed()[0] == True:
            return True
        else:
            return False