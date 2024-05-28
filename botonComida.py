import pygame
from constantes import SPRITE_BOTON_COMIDA, CENTRO_ALTO, CENTRO_ANCHO

pygame.init()

class BotonComida(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagenBoton = SPRITE_BOTON_COMIDA.subsurface((0, 0), (64, 64))
        self.click = False
        self.image = self.imagenBoton  # Correcto uso de 'image'
        self.image = pygame.transform.scale(self.image, (96, 96))  # 64 + 32
        self.posicionX = CENTRO_ANCHO - 100
        self.posicionY = CENTRO_ALTO - 200
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posicionX, self.posicionY)

    def update(self):
        pass  # No es necesario escalar la imagen nuevamente en cada actualización
