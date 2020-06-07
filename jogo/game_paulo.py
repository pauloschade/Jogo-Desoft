import pygame
from config import FPS, TITULO, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, PLAYER_WIDTH, PLAYER_HEIGHT, TILE_SIZE, GRAVITY, JUMP_SIZE, SPEED_X, STILL, JUMPING, FALLING, inimigo_height, inimigo_width, WIDTH_S, HEIGHT_S
from game_screen import game_screen
from game_screen2 import game_screen2
from game_screen3 import game_screen3
from os import path
from random import randint


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
    sucesso, bank = game_screen(screen, lives, score)
    # if sucesso != 0:
    # sucesso2, bank2 = game_screen2(screen, bank)
    # if sucesso2 != 0:
    screen_s = pygame.display.set_mode((WIDTH_S, HEIGHT_S))
    game_screen3(screen_s, bank)

finally:
    pygame.quit()

