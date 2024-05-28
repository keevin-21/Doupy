import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Doupy epic game!')
#cambiar icono
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

# Cargar el sprite y escalarlo
sprite = pygame.image.load('images/ranita-stand.png')
sprite_ancho, sprite_alto = sprite.get_size()
sprite_escalado = pygame.transform.scale(sprite, (sprite_ancho * 2, sprite_alto * 2))

sprite_rect = sprite_escalado.get_rect()
sprite_rect.topleft = (100, 100)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Configurar el reloj para controlar la velocidad del bucle
clock = pygame.time.Clock()

# Variables del juego
color_fondo = (255, 255, 255) 

def on_key_down(key):
    if key == pygame.K_LEFT:
        sprite_rect.x -= 20
    elif key == pygame.K_RIGHT:
        sprite_rect.x += 20
    elif key == pygame.K_UP:
        sprite_rect.y -= 20
    elif key == pygame.K_DOWN:
        sprite_rect.y += 20

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            on_key_down(event.key)

    # Lógica del juego
    # Aquí puedes actualizar posiciones, estados y cualquier otra lógica

    # Dibujar en la pantalla
    screen.fill(color_fondo)  # Rellenar el fondo con un color
    # Aquí puedes dibujar otros elementos del juego (e.g., sprites, texto)
    screen.blit(sprite_escalado, sprite_rect.topleft)     # Actualizar la pantalla
    pygame.display.update()

    # Controlar la velocidad del bucle (por ejemplo, 60 FPS)
    clock.tick(60)
