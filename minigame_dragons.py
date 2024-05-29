import pygame
import math

# Inicialización de Pygame
pygame.init()

# Estas constantes definen el tamaño de la ventana del juego.
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
# Establece el color de fuente en negro.
FONT_COLOR = (0, 0, 0)
# Establece el numero de huevos que se necesitan para ganar el juego.
EGG_TARGET = 20
# Establece la posición del héroe al iniciar el juego.
HERO_START = (200, 300)
# Esta es la distancia en pixeles en la que un dragón puede atacar al héroe.
ATTACK_DISTANCE = 200
# Esta es la cantidad de segundos que los dragones permanecen despiertos.
DRAGON_WAKE_TIME = 2
# Establece la cantidad de segundos que los huevos estarán ocultos.
EGG_HIDE_TIME = 2
# Este es el número de pixeles que se mueve el héroe por cada tecla oprimida.
MOVE_DISTANCE = 6
# Velocidad de la animación (cuantos fotogramas entre cambios de imagen)
ANIMATION_SPEED = 7

# Inicialización de la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Dragones")

# Inicialización de la fuente
font = pygame.font.SysFont(None, 60)
small_font = pygame.font.SysFont(None, 40)

# Carga de imágenes
dungeon_image = pygame.image.load("images/dungeon.png")
dragon_asleep_image = pygame.image.load("images/dragon-asleep.png")
dragon_awake_image = pygame.image.load("images/dragon-awake.png")
one_egg_image = pygame.image.load("images/one-egg.png")
two_eggs_image = pygame.image.load("images/two-eggs.png")
three_eggs_image = pygame.image.load("images/three-eggs.png")
egg_count_image = pygame.image.load("images/egg-count.png")
life_count_image = pygame.image.load("images/life-count.png")

link_images = {
    "parado": pygame.image.load("images/sprites_link/link_parado.png"),
    "derecha": [pygame.image.load("images/sprites_link/link_derecha.png")] + [pygame.image.load(f"images/sprites_link/link_derecha{i}.png") for i in range(1, 3)],
    "izquierda": [pygame.image.load("images/sprites_link/link_izquierda.png")] + [pygame.image.load(f"images/sprites_link/link_izquierda{i}.png") for i in range(1, 3)],
    "abajo": [pygame.image.load("images/sprites_link/link_abajo.png")] + [pygame.image.load(f"images/sprites_link/link_abajo{i}.png") for i in range(1, 3)],
    "arriba": [pygame.image.load("images/sprites_link/link_arriba.png")] + [pygame.image.load(f"images/sprites_link/link_arriba{i}.png") for i in range(1, 3)]
}

# Estado del juego
lives = 3
eggs_collected = 0
game_over = False
game_complete = False
reset_required = False

# Estructura de la guarida
easy_lair = {
    "dragon": {"image": dragon_asleep_image, "pos": (500, 190)},
    "eggs": {"image": one_egg_image, "pos": (480, 280)},
    "egg_count": 1,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 10,
    "sleep_counter": 0,
    "wake_counter": 0
}

medium_lair = {
    "dragon": {"image": dragon_asleep_image, "pos": (520, 30)},
    "eggs": {"image": two_eggs_image, "pos": (480, 100)},
    "egg_count": 2,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 7,
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair = {
    "dragon": {"image": dragon_asleep_image, "pos": (520,370)},
    "eggs": {"image": three_eggs_image, "pos": (480, 450)},
    "egg_count": 3,
    "egg_hidden": False,
    "egg_hide_counter": 0,
    "sleep_length": 4,
    "sleep_counter": 0,
    "wake_counter": 0
}

lairs = [easy_lair, medium_lair, hard_lair]

link = {"image": link_images["parado"], "pos": list(HERO_START), "rect": pygame.Rect(HERO_START, (link_images["parado"].get_width(), link_images["parado"].get_height()))}

# Índices para animación
index_derecha = 0
index_izquierda = 0
index_abajo = 0
index_arriba = 0
animation_counter = 0

def draw():
    global lairs, eggs_collected, lives, game_complete

    screen.blit(dungeon_image, (0, 0))

    if game_over:
        text = font.render("GAME OVER", True, FONT_COLOR)
        screen.blit(text, text.get_rect(center=CENTER))
    elif game_complete:
        text = font.render("GANASTE!", True, FONT_COLOR)
        screen.blit(text, text.get_rect(center=CENTER))
    else:
        screen.blit(link["image"], link["pos"])
        draw_lairs(lairs)
        draw_counters(eggs_collected, lives)

def draw_lairs(lairs_to_draw):
    for lair in lairs_to_draw:
        screen.blit(lair["dragon"]["image"], lair["dragon"]["pos"])
        if not lair["egg_hidden"]:
            screen.blit(lair["eggs"]["image"], lair["eggs"]["pos"])

def draw_counters(eggs_collected, lives):
    screen.blit(egg_count_image, (0, HEIGHT - 30))
    egg_text = small_font.render(str(eggs_collected), True, FONT_COLOR)
    screen.blit(egg_text, (30, HEIGHT - 30))
    screen.blit(life_count_image, (60, HEIGHT - 30))
    life_text = small_font.render(str(lives), True, FONT_COLOR)
    screen.blit(life_text, (90, HEIGHT - 30))

def handle_movement(keys):
    global index_derecha, index_izquierda, index_abajo, index_arriba, animation_counter

    if animation_counter >= ANIMATION_SPEED:
        animation_counter = 0

        if keys[pygame.K_RIGHT]:
            link["image"] = link_images["derecha"][index_derecha]
            link["pos"][0] += MOVE_DISTANCE
            index_derecha = (index_derecha + 1) % len(link_images["derecha"])

            if link["pos"][0] > WIDTH:
                link["pos"][0] = WIDTH

        elif keys[pygame.K_LEFT]:
            link["image"] = link_images["izquierda"][index_izquierda]
            link["pos"][0] -= MOVE_DISTANCE
            index_izquierda = (index_izquierda + 1) % len(link_images["izquierda"])

            if link["pos"][0] < 0:
                link["pos"][0] = 0

        elif keys[pygame.K_DOWN]:
            link["image"] = link_images["abajo"][index_abajo]
            link["pos"][1] += MOVE_DISTANCE
            index_abajo = (index_abajo + 1) % len(link_images["abajo"])

            if link["pos"][1] > HEIGHT:
                link["pos"][1] = HEIGHT

        elif keys[pygame.K_UP]:
            link["image"] = link_images["arriba"][index_arriba]
            link["pos"][1] -= MOVE_DISTANCE
            index_arriba = (index_arriba + 1) % len(link_images["arriba"])

            if link["pos"][1] < 0:
                link["pos"][1] = 0

        link["rect"].topleft = link["pos"]
    else:
        animation_counter += 1

def check_for_collisions():
    global lairs, eggs_collected, lives, reset_required, game_complete
    for lair in lairs:
        if not lair["egg_hidden"]:
            check_for_egg_collision(lair)
        if lair["dragon"]["image"] == dragon_awake_image and not reset_required:
            check_for_dragons_collision(lair)

def check_for_dragons_collision(lair):
    x_distance = link["pos"][0] - lair["dragon"]["pos"][0]
    y_distance = link["pos"][1] - lair["dragon"]["pos"][1]
    distance = math.hypot(x_distance, y_distance)
    if distance < ATTACK_DISTANCE:
        handle_dragon_collision()

def handle_dragon_collision():
    global reset_required
    reset_required = True
    link["pos"] = list(HERO_START)
    substract_life()

def check_for_egg_collision(lair):
    global eggs_collected, game_complete
    egg_rect = pygame.Rect(lair["eggs"]["pos"], lair["eggs"]["image"].get_size())
    if link["rect"].colliderect(egg_rect):
        lair["egg_hidden"] = True
        eggs_collected += lair["egg_count"]
        if eggs_collected >= EGG_TARGET:
            game_complete = True

def substract_life():
    global lives, game_over, reset_required
    lives -= 1
    if lives <= 0:
        game_over = True
    else:
        reset_required = False

def update_lairs():
    global lairs, link, lives
    for lair in lairs:
        if lair["dragon"]["image"] == dragon_asleep_image:
            update_sleeping_dragon(lair)
        elif lair["dragon"]["image"] == dragon_awake_image:
            update_awake_dragon(lair)

        update_egg(lair)

def update_sleeping_dragon(lair):
    if lair["sleep_counter"] >= lair["sleep_length"]:
        lair["dragon"]["image"] = dragon_awake_image
        lair["sleep_counter"] = 0
    else:
        lair["sleep_counter"] += 1

def update_awake_dragon(lair):
    if lair["wake_counter"] >= DRAGON_WAKE_TIME:
        lair["dragon"]["image"] = dragon_asleep_image
        lair["wake_counter"] = 0
    else:
        lair["wake_counter"] += 1

def update_egg(lair):
    if lair["egg_hidden"]:
        if lair["egg_hide_counter"] >= EGG_HIDE_TIME:
            lair["egg_hidden"] = False
            lair["egg_hide_counter"] = 0
        else:
            lair["egg_hide_counter"] += 1

# Configurar un temporizador para actualizar la lógica de las guaridas
pygame.time.set_timer(pygame.USEREVENT, 1000)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            update_lairs()

    keys = pygame.key.get_pressed()
    handle_movement(keys)
    check_for_collisions()

    draw()
    pygame.display.flip()

pygame.quit()
