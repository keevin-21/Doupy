import pygame

class Boton:
    def __init__(self, x, y, ancho, alto, texto, accion):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.accion = accion

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, (0, 0, 0), self.rect)
        # botones
        # ejemplo:
        font = pygame.font.Font(None, 36)
        text = font.render(self.texto, True, (255, 255, 255))
        pantalla.blit(text, (self.rect.x + 10, self.rect.y + 10))

    def isClick(self, pos):
        return self.rect.collidepoint(pos)