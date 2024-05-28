import pygame
import math

# Inicializa Pygame
pygame.init()

def minigame_dragons():
    # Configuración de la pantalla
    WIDTH = 800
    HEIGHT = 600
    CENTER_X = WIDTH // 2
    CENTER_Y = HEIGHT // 2
    CENTER = (CENTER_X, CENTER_Y)

    # Colores y otras constantes
    FONT_COLOR = (0, 0, 0)
    EGG_TARGET = 20
    HERO_START = (200, 300)
    ATTACK_DISTANCE = 200
    DRAGON_WAKE_TIME = 2
    EGG_HIDE_TIME = 2
    MOVE_DISTANCE = 3

    # Configuración de la pantalla y reloj
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Minigame: Dragons")
    clock = pygame.time.Clock()

    # Carga de imágenes
    dragon_asleep_image = pygame.image.load("images/dragon-asleep.png")
    dragon_awake_image = pygame.image.load("images/dragon-awake.png")
    dungeon_image = pygame.image.load("images/dungeon.png")
    egg_count_image = pygame.image.load("images/egg-count.png")
    life_count_image = pygame.image.load("images/life-count.png")
    link_image = pygame.image.load("images/link_parado.png")
    one_egg_image = pygame.image.load("images/one-egg.png")
    two_eggs_image = pygame.image.load("images/two-eggs.png")
    three_eggs_image = pygame.image.load("images/three-eggs.png")

    link_derecha_images = [pygame.image.load(f"images/link_derecha{i}.png") for i in range(1,3)]
    link_izquierda_images = [pygame.image.load(f"images/link_izquierda{i}.png") for i in range(1,3)]
    link_abajo_images = [pygame.image.load(f"images/link_abajo{i}.png") for i in range(1,3)]
    link_arriba_images = [pygame.image.load(f"images/link_arriba{i}.png") for i in range(1,3)]

    # Variables del juego
    lives = 3
    eggs_collected = 0
    game_over = False
    game_complete = False
    reset_required = False

    # Definición de las guaridas
    easy_lair = {
        "dragon": {"image": dragon_asleep_image, "rect": dragon_asleep_image.get_rect(topleft=(600, 100))},
        "eggs": {"image": one_egg_image, "rect": one_egg_image.get_rect(topleft=(400, 100))},
        "egg_count": 1,
        "egg_hidden": False,
        "egg_hide_counter": 0,
        "sleep_length": 10,
        "sleep_counter": 0,
        "wake_counter": 0
    }

    medium_lair = {
        "dragon": {"image": dragon_asleep_image, "rect": dragon_asleep_image.get_rect(topleft=(600, 300))},
        "eggs": {"image": two_eggs_image, "rect": two_eggs_image.get_rect(topleft=(400, 300))},
        "egg_count": 2,
        "egg_hidden": False,
        "egg_hide_counter": 0,
        "sleep_length": 7,
        "sleep_counter": 0,
        "wake_counter": 0
    }

    hard_lair = {
        "dragon": {"image": dragon_asleep_image, "rect": dragon_asleep_image.get_rect(topleft=(600, 500))},
        "eggs": {"image": three_eggs_image, "rect": three_eggs_image.get_rect(topleft=(400, 500))},
        "egg_count": 3,
        "egg_hidden": False,
        "egg_hide_counter": 0,
        "sleep_length": 4,
        "sleep_counter": 0,
        "wake_counter": 0
    }

    lairs = [easy_lair, medium_lair, hard_lair]

    link = {"image": link_image, "rect": link_image.get_rect(topleft=HERO_START)}

    # Función para dibujar en pantalla
    def draw():
        global lairs, eggs_collected, lives, game_complete

        screen.blit(dungeon_image, (0, 0))

        if game_over:
            draw_text("GAME OVER", CENTER, 60, FONT_COLOR)
        elif game_complete:
            draw_text("GANASTE!", CENTER, 60, FONT_COLOR)
        else:
            screen.blit(link["image"], link["rect"].topleft)
            draw_lairs(lairs)
            draw_counters(eggs_collected, lives)

    def draw_text(text, position, size, color):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        rect = text_surface.get_rect(center=position)
        screen.blit(text_surface, rect.topleft)

    def draw_lairs(lairs_to_draw):
        for lair in lairs_to_draw:
            screen.blit(lair["dragon"]["image"], lair["dragon"]["rect"].topleft)
            if not lair["egg_hidden"]:
                screen.blit(lair["eggs"]["image"], lair["eggs"]["rect"].topleft)

    def draw_counters(eggs_collected, lives):
        screen.blit(egg_count_image, (0, HEIGHT - 30))
        draw_text(str(eggs_collected), (30, HEIGHT - 30), 30, FONT_COLOR)
        screen.blit(life_count_image, (60, HEIGHT - 30))
        draw_text(str(lives), (90, HEIGHT - 30), 40, FONT_COLOR)

    # Variables de animación del héroe
    index_derecha = 0
    index_izquierda = 0
    index_abajo = 0
    index_arriba = 0

    def handle_movement(lairs):
        global index_derecha, index_izquierda, index_abajo, index_arriba

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            link["image"] = link_derecha_images[index_derecha]
            link["rect"].x += MOVE_DISTANCE
            index_derecha = (index_derecha + 1) % len(link_derecha_images)
            if link["rect"].right > WIDTH:
                link["rect"].right = WIDTH

        elif keys[pygame.K_LEFT]:
            link["image"] = link_izquierda_images[index_izquierda]
            link["rect"].x -= MOVE_DISTANCE
            index_izquierda = (index_izquierda + 1) % len(link_izquierda_images)
            if link["rect"].left < 0:
                link["rect"].left = 0

        elif keys[pygame.K_DOWN]:
            link["image"] = link_abajo_images[index_abajo]
            link["rect"].y += MOVE_DISTANCE
            index_abajo = (index_abajo + 1) % len(link_abajo_images)
            if link["rect"].bottom > HEIGHT:
                link["rect"].bottom = HEIGHT

        elif keys[pygame.K_UP]:
            link["image"] = link_arriba_images[index_arriba]
            link["rect"].y -= MOVE_DISTANCE
            index_arriba = (index_arriba + 1) % len(link_arriba_images)
            if link["rect"].top < 0:
                link["rect"].top = 0
        check_for_collisions(lairs)

    def check_for_collisions(lairs):
        global eggs_collected, lives, reset_required, game_complete
        for lair in lairs:
            if not lair["egg_hidden"]:
                check_for_egg_collision(lair)
            if lair["dragon"]["image"] == dragon_awake_image and not reset_required:
                check_for_dragon_collision(lair)


    def check_for_dragon_collision(lair):
        x_distance = link["rect"].centerx - lair["dragon"]["rect"].centerx
        y_distance = link["rect"].centery - lair["dragon"]["rect"].centery
        distance = math.hypot(x_distance, y_distance)
        if distance < ATTACK_DISTANCE:
            handle_dragon_collision()

    def handle_dragon_collision():
        global reset_required
        reset_required = True
        link["rect"].topleft = HERO_START
        substract_life()

    def check_for_egg_collision(lair):
        global eggs_collected, game_complete
        if link["rect"].colliderect(lair["eggs"]["rect"]):
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
        global lairs
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

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_movement()
        update_lairs()
        draw()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()