import pygame,sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Doupy El Pou tercermundista")

BLANCO = (255, 255, 255)
NEGRO = (0,0,0)
AZUL = (0,0,255)
screen.fill(BLANCO)

rectangulo = pygame.draw.rect(screen,NEGRO,(200,100,400,200))

pygame.draw.line(screen, AZUL,(200,100),(400,100),30)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()