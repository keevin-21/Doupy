import pygame
import pgzero
import pgzrun
import math


#Estas constantes definen el tamaño de la ventana del juego.
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
#Establece el color de fuente en negro.
FONT_COLOR = (0, 0, 0)
#Establece el numero de huevos que se necesitan para ganas el juego.
EGG_TARGET = 20
#Establece la posicion del heroe al iniciar el juego.
HERO_START = (200, 300)
#Esta es la distancia en pixeles en la que un dragon puede atacar al heroe.
ATTACK_DISTANCE = 200
#Esta es la cantidad de segundos que los dragones permanecen despiertos.
DRAGON_WAKE_TIME = 2
#Establece la cantidad de segundos que los huevos estaran ocultos.
EGG_HIDE_TIME = 2
#Este es el numero de pixeles que se mueve el heroe por cada tecla oprimida.
MOVE_DISTANCE = 3


#Esta variable rastrea el numero de vidas restantes.
lives = 3 
#Rastrea el numeros de huevos recolectados.
eggs_collected = 0
#Esta variable rastrea si el juego ha terminado.
game_over = False
#Esta variable rastrea si el jugador ha ganado.
game_complete = False
reset_required = False

easy_lair = {
    #Estas son las coordenadas del dragon en esta guarida.
    "dragon": Actor("dragon-asleep", pos=(600, 100)),
    #esto establece las coordenadas de un huevo.
    "eggs": Actor("one-egg", pos=(400,100)),
    #Esto establece la cantidad de huevos para la guarida.
    "egg_count": 1,
    #Esto comprueba si el huevo esta actualmente escondido.
    "egg_hidden": False,
    #Esto rastrea cuantos segundos ha estado oculto el huevo.
    "egg_hide_counter": 0,
    #Esto rastrea el ciclo de sueño del dragon.
    "sleep_length": 10,
    "sleep_counter": 0,
    "wake_counter": 0
}

medium_lair = {
    #Estas son las coordenadas del dragon en esta guarida.
    "dragon": Actor("dragon-asleep", pos=(600, 300)),
    #esto establece las coordenadas de los huevos.
    "eggs": Actor("two-eggs", pos=(400,300)),
    #Esto establece la cantidad de huevos para la guarida.
    "egg_count": 2,
    #Esto comprueba si los huevos estan actualmente escondidos.
    "egg_hidden": False,
    #Esto rastrea cuantos segundos han estados ocultos los huevos.
    "egg_hide_counter": 0,
    #Esto rastrea el ciclo de sueño del dragon.
    "sleep_length": 7,
    "sleep_counter": 0,
    "wake_counter": 0
}

hard_lair = {
    #Estas son las coordenadas del dragon en esta guarida.
    "dragon": Actor("dragon-asleep", pos=(600, 500)),
    #esto establece las coordenadas de los huevos.
    "eggs": Actor("three-eggs", pos=(400,500)),
    #Esto establece la cantidad de huevos para la guarida.
    "egg_count": 3,
    #Esto comprueba si los huevos estan actualmente escondidos.
    "egg_hidden": False,
    #Esto rastrea cuantos segundos han estados ocultos los huevos.
    "egg_hide_counter": 0,
    #Esto rastrea el ciclo de sueño del dragon.
    "sleep_length": 4,
    "sleep_counter": 0,
    "wake_counter": 0
}

lairs = [easy_lair, medium_lair, hard_lair]

link = Actor("link_parado", pos=HERO_START)


def draw():
    global lairs,eggs_collected, lives, game_complete
    
    screen.clear()
    screen.blit("dungeon", (0, 0))
    
    if game_over:
        screen.draw.text("GAME OVER", fontsize=60, center=CENTER, color=FONT_COLOR)
    elif game_complete:
        screen.draw.text("GANASTE!", fontsize=60, center=CENTER, color=FONT_COLOR)
    else:
        link.draw()
        draw_lairs(lairs)
        draw_counters(eggs_collected,lives)
    

    

def draw_lairs(lairs_to_draw):
    for lair in lairs_to_draw:
        lair["dragon"].draw()
        if lair["egg_hidden"] == False:
            lair["eggs"].draw()

def draw_counters(eggs_collected, lives):
    screen.blit("egg-count",(0,HEIGHT-30))
    screen.draw.text(str(eggs_collected),
                        fontsize=30,
                        color=FONT_COLOR,
                        topleft=(30,HEIGHT-30))
    screen.blit("life-count",(60,HEIGHT-30))
    screen.draw.text(str(lives),
                        fontsize=40,
                        color=FONT_COLOR,
                        pos=(90,HEIGHT-30))

#MOVIMIENTO DEL HEROE

caminando_derecha = ["link_derecha", "link_derecha1", "link_derecha2", "link_derecha3"]
index_derecha = 0
caminando_izquierda = ["link_izquierda", "link_izquierda1", "link_izquierda2", "link_izquierda3"]
index_izquierda = 0
caminando_abajo = ["link_abajo", "link_abajo1", "link_abajo2"]
index_abajo = 0
caminando_arriba = ["link_arriba", "link_arriba1", "link_arriba2"]
index_arriba = 0

def update():
    global index_derecha, index_izquierda, index_arriba,index_abajo
    if keyboard.right:
        link.image = caminando_derecha[index_derecha]
        link.x += MOVE_DISTANCE
        index_derecha = (index_derecha + 1) % len(caminando_derecha)

        if link.x > WIDTH:
            link.x = WIDTH
        
    elif keyboard.left:
        link.image = caminando_izquierda[index_izquierda]
        link.x -= MOVE_DISTANCE
        index_izquierda = (index_izquierda + 1) % len(caminando_izquierda)
        
        if link.x < 0:
            link.x = 0
        
    elif keyboard.down:
        link.image = caminando_abajo[index_abajo]
        link.y += MOVE_DISTANCE
        index_abajo = (index_abajo + 1) % len(caminando_abajo)
        
        if link.y > HEIGHT:
            link.y = HEIGHT
        
    elif keyboard.up:
        link.image = caminando_arriba[index_arriba]
        link.y -= MOVE_DISTANCE
        index_arriba = (index_arriba + 1) % len(caminando_arriba)
        
        if link.y < 0:
            link.y = 0
    
    check_for_collisions()
            
            
            
###################################################################################

def check_for_collisions():
    global lairs,eggs_collected,lives,reset_required,game_complete
    for lair in lairs:
        if lair["egg_hidden"] is False:
            check_for_egg_collision(lair)
        if lair["dragon"].image == "dragon-awake" and reset_required is False:
            check_for_dragons_collision(lair)

def check_for_dragons_collision(lair):
    x_distance = link.x - lair["dragon"].x
    y_distance = link.y - lair["dragon"].y
    distance = math.hypot(x_distance, y_distance)
    if distance < ATTACK_DISTANCE:
        handle_dragon_collision()

def handle_dragon_collision():
    global reset_required
    reset_required = True
    animate(link,pos=HERO_START,on_finished=substract_life)

def check_for_egg_collision(lair):
    global eggs_collected,game_complete
    if link.colliderect(lair["eggs"]):
        lair["egg_hidden"] = True
        eggs_collected += lair["egg_count"]
        if eggs_collected >= EGG_TARGET:
            game_complete = True

def substract_life():
    global lives,game_over,reset_required
    lives -= 1
    if lives <= 0:
        game_over = True
    else:
        reset_required = False

def update_lairs():
    global lairs, link, lives
    for lair in lairs:
        if lair["dragon"].image == "dragon-asleep":
            update_sleeping_dragon(lair)
        elif lair["dragon"].image == "dragon-awake":
            update_awake_dragon(lair)
        
        update_egg(lair)    
        
clock.schedule_interval(update_lairs, 1.0)

def update_sleeping_dragon(lair):
    if lair["sleep_counter"] >= lair["sleep_length"]:
        lair["dragon"].image = "dragon-awake"
        lair["sleep_counter"] = 0
    else:
        lair["sleep_counter"] += 1

def update_awake_dragon(lair):
    if lair["wake_counter"] >= DRAGON_WAKE_TIME:
        lair["dragon"].image = "dragon-asleep"
        lair["wake_counter"] = 0
    else:
        lair["wake_counter"] += 1

def update_egg(lair):
    if lair["egg_hidden"] is True:
        if lair["egg_hide_counter"] >= EGG_HIDE_TIME:
            lair["egg_hidden"] = False
            lair["egg_hide_counter"] = 0
        else:
            lair["egg_hide_counter"] += 1

pgzrun.go()
        