# import pygame
# import sys

# pygame.init()

# screen = pygame.display.set_mode((800, 680))
# pygame.display.set_caption("Ejemplo de Pygame")

# running = True 
# while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#    
#    screen.fill((255, 255, 255))
#    pygame.display.flip()

# pygame.quit()
# sys.exit()

import pygame
# from pygame import Game
# from GameClass import Game

import sys
import time
import os
import random


# Fondo del Juego
BACKGROUND = pygame.image.load(os.path.join('img', 'background.png'))
ICON_IMAGE = pygame.image.load(os.path.join('img', 'title_icon.png'))
TITLE = 'Space Invader'

# Jugador
PLAYER_IMAGE = pygame.image.load('img/player_image.png')
BULLET_IMAGE = pygame.image.load('img/bullet_image.png')


pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON_IMAGE)


# Cargar y reproducir música de fondo
pygame.mixer.music.load('sounds/background_song.mp3')
pygame.mixer.music.play(-1)  # Repetir indefinidamente

x, y = 400, 300
vel = 5

running = True

def main():
    puntaje = 0
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    try:
        pygame.mixer.music.play(-1)
    except:
        pass



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, 50, 50))  # Dibujar un rectángulo rojo que se mueve con las teclas de flecha
    pygame.display.update() 


# Obtener el tiempo actual
start_time = time.time()


#Hacer algo que tome tiempo
time.sleep(2)


# Calcular el tiempo transcurrido
elapsed_time = time.time() - start_time
print("Tiempo transcurrido:", elapsed_time, "segundos")


# Generar un número aleatorio entre 1 y 10
random_number = random.randint(1, 10)
print("Número aleatorio:", random_number)


# Mezclar una lista
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Lista mezclada:", my_list)

current_directory = os.getcwd()
print("Directorio actual:", current_directory)

# Crear un nuevo directorio
new_directory = os.path.join(current_directory, "nuevo_directorio")
os.mkdir(new_directory)
print("Directorio creado:", new_directory)


# Listar los archivos en el directorio actual
files_in_directory = os.listdir(current_directory)
print("Archivos en el directorio:", files_in_directory)