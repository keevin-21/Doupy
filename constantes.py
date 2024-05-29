import pygame
import os
import pickle

# Inicialización de Pygame
pygame.init()

# Función para leer sprites desde una hoja de sprites
def leerSpriteSheet(primerNumero, segundoNumero, spriteSheet, anchoSprite, altoSprite):
    imagenes = []
    for i in range(primerNumero, segundoNumero):
        image = spriteSheet.subsurface((i * anchoSprite, 0), (anchoSprite, altoSprite))
        imagenes.append(image)
    return imagenes

# Función para agrupar sprites
def grupoSprites(*sprites):
    grupo = pygame.sprite.Group()
    for sprite in sprites:
        grupo.add(sprite)
    return grupo

# Función para guardar el progreso
def salvarProgreso(hambre, limpieza):
    mascota = (hambre, limpieza)
    with open('guardar_mascota.dat', 'wb') as archivo:
        pickle.dump(mascota, archivo)

# Función para recuperar el progreso
def recuperarProgreso(hambre, limpieza):
    try:
        with open('guardar_mascota.dat', 'rb') as archivo:
            mascota = pickle.load(archivo)
            archivo.close()
    except FileNotFoundError:
        mascota = (100, 100)
    return mascota

# Directorio principal
DIRECTORIO_PRINCIPAL = os.path.dirname(__file__)

# Pantalla
ANCHO_PANTALLA = 640
ALTO_PANTALLA = 480
POSICION_RELOJ = (500, 10)
RELOJ_JUEGO = pygame.time.Clock()

# Colores
NEGRO = (0, 0, 0)

# Directorios
DIRECTORIO_IMAGENES = os.path.join(DIRECTORIO_PRINCIPAL, 'sprites')
DIRECTORIO_SONIDO = os.path.join(DIRECTORIO_PRINCIPAL, 'trilha sonora')

# Cargar imágenes
SPRITE_SHEET = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, 'link_sprites.png'))
SPRITE_COMIDA = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, 'apple_sprites.png'))
SPRITE_BOTON_COMIDA = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, 'apple_button.png'))
SPRITE_BOTON_JABON = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, 'soap_button.png'))
SPRITE_JABON = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, 'soap_sprites.png'))
SPRITE_MOUSE = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, 'mouse_sprites.png'))
SPRITE_ACARICIAR = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, 'sprites_pet.png'))
SPRITE_COMER = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, 'sprites_eat.png'))
SPRITE_BARRA = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, 'bar.png'))
BACKGROUND = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, 'background.png'))

# Fuente
FUENTE_CS = pygame.font.SysFont("Arial", 40, True, True)
