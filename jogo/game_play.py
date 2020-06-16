import pygame
from config import FPS, TITULO, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, PLAYER_WIDTH, PLAYER_HEIGHT, TILE_SIZE, GRAVITY, JUMP_SIZE, SPEED_X, STILL, JUMPING, FALLING, inimigo_height, inimigo_width, WIDTH_S, HEIGHT_S, QUIT, GAME
from hist import hist
from hist2 import hist2
from game_screen import game_screen
from game_screen2 import game_screen2
from game_screen3 import game_screen3
from game_over import game_over
from win_screen import win_screen
from scoreboard_show import scoreboard
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

bank = [3, 0]
state = GAME

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load(path.join(img_dir, 'earth_land_em_pe.png')).convert()
BACKGROUND_E = pygame.transform.scale(bg, (WIDTH, HEIGHT))
# Nome do jogo
pygame.display.set_caption(TITULO)

# Imprime instruções
print('*' * len(TITULO))
print(TITULO)
print('*' * len(TITULO))
print('Utilize as setas do teclado para andar e pular.')

# Comando para evitar travamentos.
try:
    while state != QUIT:
        state = intro(screen)
        if state == GAME:
            state = hist()
            if state == GAME:
                state, init_time = instru()
                if state == GAME:
                    sucesso, bank = game_screen(screen)
                    if sucesso == 1:
                        sucesso, bank, midtime1 = game_screen2(screen, bank)
                        if sucesso == 1:
                            state = hist2()
                            if state == GAME:
                                state, midtime2 = instru2()
                                if state == GAME:
                                    screen_s = pygame.display.set_mode((WIDTH_S, HEIGHT_S))
                                    sucesso, bank, total_time = game_screen3(screen_s, bank)
                                    times = [init_time, midtime1, midtime2, total_time]
                                    if sucesso == 1:
                                        state, score, nome = win_screen(bank, times)
                                        if state == GAME:
                                            state = scoreboard(score, nome)
                                    elif sucesso == 0:
                                        state = game_over(bank)
                                    else:
                                        state = QUIT
                        elif sucesso == 0:
                            state = game_over(bank)
                        else:
                            state = QUIT
                    elif sucesso == 0:
                        state = game_over(bank)
                    else:
                        state = QUIT

finally:
    pygame.quit()
