import pygame
from constantes import SPRITE_MOUSE

pygame.init()

class Mouse(pygame.sprite.Sprite):
    def __init__(self, mousePos):
        super().__init__()
        self.click = False
        self.x, self.y = mousePos
        self.estatico = SPRITE_MOUSE.subsurface((128, 0), (64, 80))
        self.clickando = SPRITE_MOUSE.subsurface((64, 0), (64, 80))
        self.image = self.estatico
        self.image = pygame.transform.scale(self.image, (32, 40))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

    def update(self):
        if not self.click:  # Si no se está haciendo clic
            self.rect.topleft = pygame.mouse.get_pos()  # Actualizar la posición del cursor
            self.rect.x -= 32  # Ajuste de la posición del rectángulo

            if pygame.mouse.get_pressed()[0]:  # Si el botón del ratón está presionado
                self.image = self.clickando  # Cambiar a la imagen de clicar
                self.click = True  # Marcar que se está haciendo clic
            else:
                self.image = self.estatico  # Volver a la imagen estática
                self.click = False  # Marcar que no se está haciendo clic

        self.image = pygame.transform.scale(self.image, (33 * 2, 40 * 2))  # Escalar la imagen
