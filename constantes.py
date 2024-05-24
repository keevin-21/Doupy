import pygame
import os

# Inicialización de Pygame
pygame.init()

# Función para leer sprites desde una hoja de sprites
def leerSpriteSheet(iniciarCortar, finalCortar, spriteSheet, anchoSprite, altoSprite):
    imagenes = []
    for i in range(iniciarCortar, finalCortar):
        imagen = spriteSheet.subsurface((i * anchoSprite, 0), (anchoSprite, altoSprite))
        imagenes.append(imagen)
    return imagenes

# Función para agrupar sprites
def grupoSprites(*sprites):
    grupo = pygame.sprite.Group()
    for sprite in sprites:
        grupo.add(sprite)
    return grupo

# Directorio principal
DIRECTORIO_PRINCIPAL = os.path.dirname(__file__)
print(f"Directorio principal: {DIRECTORIO_PRINCIPAL}")

# Pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
CENTRO_ANCHO = ANCHO_PANTALLA / 2
CENTRO_ALTO = ALTO_PANTALLA / 2

# Reloj
RELOJ_JUEGO = pygame.time.Clock()

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Directorios
DIRECTORIO_IMAGENES = os.path.join(DIRECTORIO_PRINCIPAL, "sprites")
print("asdad", DIRECTORIO_IMAGENES)
DIRECTORIO_MUSICA = os.path.join(DIRECTORIO_PRINCIPAL, "soundtrack")

try:
    BACKGROUND_PATH = os.path.join(DIRECTORIO_IMAGENES, "background.png")
    print(f"Ruta de la imagen de fondo: {BACKGROUND_PATH}")
    BACKGROUND = pygame.image.load(BACKGROUND_PATH)
except FileNotFoundError as e:
    print(f"Error al cargar la imagen: {e}")
    pygame.quit()
    exit()

# Carga de Sprites
try:
    BACKGROUND = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, "background.png"))

    SPRITE_COMIDA = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, "apple_sprites.png"))
    SPRITE_BOTON_COMIDA = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, "apple_button.png"))

    SPRITE_JABON = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, "soap_sprites.png"))
    SPRITE_BOTON_JABON = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, "soap_button.png"))

    SPRITE_BARRA = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, "bar.png"))

    SPRITE_MOUSE = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, "mouse_sprites.png"))

    SPRITE_COMER = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, "sprites_eat.png"))
    SPRITE_ACARICIAR = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, "sprites_pet.png"))

    # Provisional
    SPRITE_LINK = pygame.image.load(os.path.join(DIRECTORIO_IMAGENES, "link_sprites.png"))
except pygame.error as e:
    print(f"Error al cargar las imágenes: {e}")
    pygame.quit()
    exit()
