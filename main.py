import pygame
from pygame.locals import *
from datetime import datetime
from sys import exit
from constantes import ANCHO_PANTALLA, ALTO_PANTALLA, BACKGROUND, RELOJ_JUEGO, FUENTE
from constantes import grupoSprites
from mascota import Doupy
from botonComida import BotonComida
from botonJabon import BotonJabon
from comida import Comida
from jabon import Jabon
from barra import Barras
from mouse import Mouse

pygame.init()
clock = RELOJ_JUEGO

pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.load("soundtrack/BGM.mp3")
pygame.mixer.music.play(-1)

# Set up display
BACKGROUND = pygame.transform.scale(BACKGROUND, (ANCHO_PANTALLA, ALTO_PANTALLA))
ventana = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Doupy")

mascota = Doupy()
botonComida = BotonComida()
botonJabon = BotonJabon()
barraComida = Barras(mascota.comer, 30, 20)
barraLimpieza = Barras(mascota.limpio, 30, 50)
barraFelicidad = Barras(mascota.felicidad, 30, 80)
mouse = Mouse(pygame.mouse.get_pos())
todosLosSprites = grupoSprites(mascota, botonComida, botonJabon, barraComida, barraLimpieza, barraFelicidad, mouse)
pararComida = False
jabonExiste = False
comidaExiste = False
grupoComida = pygame.sprite.Group()
grupoJabon = pygame.sprite.Group()
andando = True

# Game loop
running = True
while running:
    horaActual = datetime.now()
    horaTexto = horaActual.strftime("%H:%M:%S")
    horaFormateada = FUENTE.render(horaTexto, True, (255, 255, 255))

    mousePos = pygame.mouse.get_pos()
    mouseButton1 = pygame.mouse.get_pressed()
    camilla = Comida(mousePos)

    RELOJ_JUEGO.tick(60)
    ventana.fill((0, 0, 0))
    pygame.mouse.set_visible = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and botonComida.rect.collidepoint(mousePos) and not pararComida:
                todosLosSprites.add(camilla)
                pararComida = True
                comidaExiste = True

            if event.button == 1 and botonJabon.rect.collidepoint(mousePos):
                jabon = Jabon(mousePos)
                todosLosSprites.add(jabon)
                jabonExiste = True

        if event.type == pygame.USEREVENT + 2:
            pygame.time.set_timer(camilla.desaparecer, 0)
            todosLosSprites.remove(camilla)
            del camilla
            pararComida = False

        if event.type == pygame.USEREVENT + 3:
            pygame.time.set_timer(jabon.desaparecer, 0)
            todosLosSprites.remove(jabon)
            del jabon
            jabonExiste = False

        if event.type == mascota.decrementarAlimentacion:
            if mascota.alimento <= 0:
                mascota.alimento = 0
            else:
                mascota.alimento -= 5
        
            barraComida.decrecerBarra(mascota.alimento)
            barraFelicidad.decrecerBarra(mascota.felicidad)

        if event.type == mascota.decrementarLimpieza:
            if mascota.limpio <= 0:
                mascota.limpio = 0
            else:
                mascota.limpio -= 5

            barraLimpieza.decrecerBarra(mascota.limpio)
            barraFelicidad.decrecerBarra(mascota.felicidad)

        if jabonExiste:
            grupoJabon.add(jabon)
            colisiones = pygame.sprite.spritecollide(mascota, grupoJabon, False, pygame.sprite.collide_mask)

            if colisiones:
                jabon.usando = False

        if comidaExiste:
            if camilla.comidaTirada:
                grupoComida.add(camilla)
                colisiones2 = pygame.sprite.spritecollide(mascota, grupoComida, False, pygame.sprite.collide_mask)

                if colisiones2:
                    camilla.siendoComido()
                
                if camilla.fueComido:
                    if mascota.alimento >= 150:
                        mascota.alimento = 150
                    else:
                        mascota.alimento -= 10

                    barraComida.decrecerBarra(mascota.alimento)
                    pygame.time.set_timer(camilla.desaparecer, 0)
                    mascota.comer = False
                    comidaExiste = False

    if mouseButton1[0] and mascota.rect.collidepoint(mousePos):
        mascota.updateAction(2)

    ventana.blit(BACKGROUND, (0, 0))
    ventana.blit(horaFormateada, (500, 10))
    todosLosSprites.draw(ventana)
    todosLosSprites.update()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

import pygame
from pygame.locals import *
from datetime import datetime
from sys import exit
from constantes import ANCHO_PANTALLA, ALTO_PANTALLA, BACKGROUND, RELOJ_JUEGO
from constantes import grupoSprites
from mascota import Doupy
from botonComida import BotonComida
from botonJabon import BotonJabon
from comida import Comida
from jabon import Jabon
from barra import Barras
from mouse import Mouse
from random import randint


pygame.init()
clock = RELOJ_JUEGO

pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.load("soundtrack/BGM.mp3")
pygame.mixer.music.play(-1)

# Set up display
BACKGROUND = pygame.transform.scale(BACKGROUND, (ANCHO_PANTALLA, ALTO_PANTALLA))
ventana = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Doupy")

mascota = Doupy()
botonComida = BotonComida()
botonJabon = BotonJabon()
barraComida = Barras(mascota.comer, 30, 20)
barraLimpieza = Barras(mascota.limpio, 30, 50)
barraFelicidad = Barras(mascota.felicidad, 30, 80)
mouse = Mouse(pygame.mouse.get_pos())
todosLosSprites = grupoSprites(mascota, botonComida, botonJabon, barraComida, barraLimpieza, barraFelicidad, mouse)
pararComida = False
jabonExiste = False
comidaExiste = False
grupoComida = pygame.sprite.Group()
grupoJabon = pygame.sprite.Group()



# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ventana.blit(BACKGROUND, (0, 0))
    pygame.display.update()

    clock.tick(60)

pygame.quit()
