import pygame
from config import FPS, TITULO, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, PLAYER_WIDTH, PLAYER_HEIGHT, TILE_SIZE, GRAVITY, JUMP_SIZE, SPEED_X, STILL, JUMPING, FALLING, inimigo_height, inimigo_width, WIDTH_S, HEIGHT_S, INIT, QUIT, INIT2, GAME
from game_screen import game_screen
from game_screen2 import game_screen2
from game_screen3 import game_screen3
from os import path
from random import randint
from game_intro import intro
from instru import instru
from instru2 import instru2


pygame.init()
pygame.mixer.init()

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2 

lives = 3
score = 0

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load(path.join(img_dir, 'earth_land_em_pe.png')).convert()
BACKGROUND_E = pygame.transform.scale(bg, (WIDTH, HEIGHT))
# Nome do jogo
pygame.display.set_caption(TITULO)

# Imprime instruções
print('*' * len(TITULO))
print(TITULO.upper())
print('*' * len(TITULO))
print('Utilize as setas do teclado para andar e pular.')

# Comando para evitar travamentos.
try:
    sucesso = 1
    state = INIT
    if state == INIT:
        state = intro(screen)
        if state == INIT2:
            state = instru()
            if state == GAME:
                sucesso, bank = game_screen(screen, lives, score)
                if sucesso != 0:
<<<<<<< HEAD
                    sucesso2, bank2 = game_screen2(screen, bank)
                    if sucesso2 != 0:
                        state = instru2()
                        if state == GAME:
                            screen_s = pygame.display.set_mode((WIDTH_S, HEIGHT_S))
                            game_screen3(screen_s, bank2)
=======
                    sucesso, bank = game_screen2(screen, bank)
                    if sucesso != 0:
                        screen_s = pygame.display.set_mode((WIDTH_S, HEIGHT_S))
                        game_screen3(screen_s, bank)

>>>>>>> d509465791ab0d997d8d6236ce59e3803a8f85c1
finally:
    pygame.quit()
