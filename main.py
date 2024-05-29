import pygame
from pygame.locals import *
from sys import exit
from random import randint
from datetime import datetime
from mascota import Mascota
from barra import Barras
from botonComida import BotonComida
from botonJabon import BotonJabon
from comida import Comida
from jabon import Jabon
from mouse import Mouse
from constantes import recuperarProgreso, salvarProgreso, leerSpriteSheet, grupoSprites, BACKGROUND, ALTO_PANTALLA, ANCHO_PANTALLA, RELOJ_JUEGO, NEGRO, FUENTE_CS, POSICION_RELOJ

pygame.init() 
pygame.mixer.music.set_volume(0)
pygame.mixer.music.load("soundtrack/BGM.mp3")
pygame.mixer.music.play(-1)

BACKGROUND = pygame.transform.scale(BACKGROUND, (ANCHO_PANTALLA, ALTO_PANTALLA))
ventana = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("DOUPY")

mascota = Mascota()
mascota.hambre, mascota.limpieza = recuperarProgreso(mascota.hambre, mascota.limpieza)
botonComida = BotonComida()
botonJabon = BotonJabon()
barraComida = Barras(mascota.hambre, 30, 20)
barraLimpieza = Barras(mascota.limpieza, 30, 50)
barraFelicidad = Barras(mascota.felicidad, 30, 80)
mouse = Mouse(pygame.mouse.get_pos())
todosLosSprites = grupoSprites(botonJabon, mascota, botonComida, barraComida, barraFelicidad, barraLimpieza, mouse)
pararComida = False
comidaExiste = False
jabonExiste = False
grupoComida = pygame.sprite.Group()
grupoJabon = pygame.sprite.Group()
continuarCaminando = True

while True:
    horaActual = datetime.now()
    horaEnTexto = horaActual.strftime("%H:%M")
    horaFormato = FUENTE_CS.render(horaEnTexto, True, (255, 255, 255))

    mousePos = pygame.mouse.get_pos()
    mouseButton = pygame.mouse.get_pressed()[0]
    RELOJ_JUEGO.tick(60)
    ventana.fill(NEGRO)
    pygame.mouse.set_visible(False)

    for event in pygame.event.get():
        if event.type == QUIT:
            salvarProgreso(mascota.hambre, mascota.limpieza)
            pygame.quit()
            exit()

        if continuarCaminando == True:
            if event.type == mascota.temporizadorAndar:
                mascota.nuevoX = randint(0, 600)
                mascota.nuevoY = randint(200, 350)

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and botonComida.rect.collidepoint(mousePos) and pararComida == False:
                maca = Comida(mousePos)
                todosLosSprites.add(maca)
                pararComida = True
                comidaExiste = True

            if event.button == 1 and botonJabon.rect.collidepoint(mousePos):
                jabon = Jabon(mousePos)
                todosLosSprites.add(jabon)
                jabonExiste = True
        
        if event.type == pygame.USEREVENT + 2:
            pygame.time.set_timer(maca.desaparecer, 0)
            todosLosSprites.remove(maca)
            comidaExiste = False
            del maca
            pararComida = False

        if event.type == pygame.USEREVENT + 3:
            pygame.time.set_timer(jabon.desaparecer, 0)
            todosLosSprites.remove(jabon)
            del jabon
            jabonExiste = False

        if event.type == mascota.bajarHambre:
            if mascota.hambre <= 0:
                mascota.hambre = 0
            else:
                mascota.hambre -= 10

            barraComida.bajarBarra(mascota.hambre)
            barraFelicidad.bajarBarra(mascota.felicidad)

        if event.type == mascota.bajarLimpieza:
            if mascota.limpieza <= 0:
                mascota.limpieza = 0
            else:
                mascota.limpieza -= 10

            barraLimpieza.bajarBarra(mascota.limpieza)
            barraFelicidad.bajarBarra(mascota.felicidad)
        
        if jabonExiste == True:
            grupoJabon.add(jabon)
            colisiones = pygame.sprite.spritecollide(mascota, grupoJabon, False, pygame.sprite.collide_mask)

            if colisiones:
                jabon.usando = True
                if mascota.limpieza >= 150:
                    mascota.limpieza = 150
                else:
                    mascota.limpieza += 1

                barraLimpieza.subirBarra(mascota.limpieza)
            else:
                jabon.usando = False

        if comidaExiste == True:
            if maca.comidaTirada == True:
                continuarCaminando = False
                mascota.nuevoX = maca.rect.x - 64
                mascota.nuevoY = maca.rect.y - 64
                
                grupoComida.add(maca)
                colisiones2 = pygame.sprite.spritecollide(maca, grupoComida, False, pygame.sprite.collide_mask)
                
                if colisiones2:
                    mascota.nuevoX = mascota.rect
                    mascota.nuevoY = mascota.rect
                    mascota.comiendo = True
                    maca.siendoComido()
                if maca.fueComido == True:
                    if mascota.hambre >= 150:
                        mascota.hambre = 150
                    else:
                        mascota.hambre += 10
                        

                    barraComida.subirBarra(mascota.hambre)
                    pygame.time.set_timer(maca.desaparecer, 100)
                    mascota.comiendo = False
                    continuarCaminando = True
                    comidaExiste = False

    if mouseButton == True and mascota.rect.collidepoint(mousePos):
        continuarCaminando = False
        mascota.actualizarAccion(0) # 5
        mascota.nuevoX = mascota.rect.x
        mascota.nuevoY = mascota.rect.y

    if mascota.action == 0:
        continuarCaminando = True

    ventana.blit(BACKGROUND, (0, 0))
    ventana.blit(horaFormato, POSICION_RELOJ)
    todosLosSprites.draw(ventana)
    todosLosSprites.update()
    pygame.display.flip()
                