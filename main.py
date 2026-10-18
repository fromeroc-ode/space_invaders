import pygame
from pygame import mixer
from GameClass import Game
import os
from PlayerClass import Player
from EnemyClass import Enemy
from DrawingClass import Drawing
from VentanaNombre import PantallaNombre
from MenuPrincipalClass import MenuPrincipal
from AcercaDeMenuClass import MenuAcercaDe
from MenuPuntajeClass import MenuPuntajes
# Background:
BACKGROUND = pygame.image.load(os.path.join('img', 'background.png'))
ICON_IMAGE = pygame.image.load(os.path.join('img', 'title_icon.png'))
TITLE = 'Space Invaders'
game_muted = False

# Player:
    # Images
PLAYER_IMAGE = pygame.image.load(os.path.join('img', 'player_image.png'))
BULLET_IMAGE = pygame.image.load(os.path.join('img', 'bullet_image.png'))
    # SFX

pygame.init()
# Game window
WIDTH, HEIGTH = 500, 900
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON_IMAGE)
try:
    mixer.music.load('sounds/background_song.mp3')
    
except:
    print("No se pudo cargar el sonido")
    pass


def main():
    puntaje = 0
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    try:
        mixer.music.set_volume(0 if game_muted else 1)
        mixer.music.play(-1)
    except:
        pass

    # Instancing the Game
    font = pygame.font.SysFont('comicsans', 50)
    game = Game(font, FPS,  3, WIN, WIDTH, HEIGTH, 0, clock)
    
    # Player properties and Instancing it
    player_x = ((WIDTH)-(PLAYER_IMAGE.get_width())) / 2
    player_y = HEIGTH - PLAYER_IMAGE.get_height() - 20
    player = Player(x= player_x, y= player_y, x_speed= 10, y_speed= 4)

    # Enemyes properties and Instancing it in a list of enemies
    enemy_init = Enemy(speed = 4)
    enemy_wave = 4
    enemies = enemy_init.create(1, WIDTH)
    enemies_to_spawn = enemy_wave - len(enemies)
    spawn_timer = FPS

    # Drawing
    draw = Drawing(WIN) 
    draw.drawing(game, player, enemies, FPS= 60, puntos=0)


    while run:
        clock.tick(FPS)
       
        # Game Over
        if game.over():
            if puntaje > game.max_pun:
                sound = pygame.mixer.Sound("sounds/ganar.mp3")
                sound.set_volume(0 if game_muted else 1)
                sound.play()
                PantallaNombre(puntaje)
            MenuPuntajes(menu_principal).ejecutar()
            return
        # Quitting the game
        if game.escape():
            run = False
            continue
          
        # Increasing the Level
        if not enemies and enemies_to_spawn == 0:
            game.level += 1
            enemy_wave += 1
            enemy_init.increase_speed()
            player.increase_speed()
            enemies_to_spawn = enemy_wave
            spawn_timer = 0
            if game.level % 5 == 0:
                player.increase_reload_speed()
            if game.level % 3 == 0:
                if player.max_amount_bullets < 10:
                    player.max_amount_bullets += 1

        if enemies_to_spawn > 0:
            if spawn_timer <= 0:
                enemies.extend(enemy_init.create(1, WIDTH))
                enemies_to_spawn -= 1
                spawn_timer = max(FPS // 4, FPS - (game.level - 1) * 5)
            else:
                spawn_timer -= 1
        
        # Player Movement
        player.move(WIDTH, HEIGTH)
        player.create_bullets()
        game.reload_bullet(len(player.bullets))
        player.cooldown()

        # Enemy Movement
        for enemy in enemies[:]:
            enemy.move()
            if enemy.y + enemy.get_height() >= game.HEIGTH:
                game.lives -= 1
                enemies.remove(enemy)
                continue
            if player.collides_with(enemy):
                game.lives -= 1
                enemies.remove(enemy)
                continue
            if player.hit(enemy):
                enemies.remove(enemy)
                player.fired_bullets.pop(0)
                crash_sound = pygame.mixer.Sound("sounds/explosion.wav")
                crash_sound.set_volume(0 if game_muted else 1)
                puntaje += 1
                crash_sound.play()
                continue

        draw.drawing(game, player, enemies, FPS, puntaje)


def initGame():
    main()

def initPuntaje():
    menu_puntajes = MenuPuntajes(menu_principal).ejecutar()


def initAbout():
    menu_puntajes = MenuAcercaDe(menu_principal).ejecutar()

def set_game_muted(muted):
    global game_muted
    game_muted = muted
    mixer.music.set_volume(0 if game_muted else 1)

def toggle_game_mute():
    set_game_muted(not game_muted)
    return game_muted

def menu_principal():
    MenuPrincipal(
        initGame,
        initPuntaje,
        initAbout,
        toggle_game_mute,
        lambda: game_muted,
    ).menu_principal()

menu_principal()
