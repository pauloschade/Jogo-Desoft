import pygame
import os
from config import PLAYER_WIDTH, PLAYER_HEIGHT, img_dir, TILE_SIZE, inimigo_height, inimigo_width, VILAO_HEIGHT, VILAO_WIDHT, ATTACK_HEIGHT, ATTACK_WIDTH, T_ATTACK_HEIGHT, T_ATTACK_WIDTH, FLAG_WIDTH, FLAG_HEIGHT

#imagens
BACKGROUND_E = 'background'
PLAYER_IMG_R = 'player_img_r'
PLAYER_IMG_L = 'player_img_l'
INIMIGO_IMG = 'perry'
VILAO_IMG = "vilao_img"
RIGHT_ATTACK = 'right_attack'
LEFT_ATTACK = 'left_attack'
TOSHI_ATTACK = 'toshi attack'
FLAG = 'flag'
SCORE_FONT = 'score_font'
BACKGROUND_L = "lava_1"


#tipo de tile
BLOCK = 0
EMPTY = -1
MAP2 = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
]




MAP = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
]


def load_assets():
    assets = {}
    assets[BACKGROUND_E] =  pygame.image.load(os.path.join(img_dir, 'earth_land_em_pe.png')).convert_alpha()
    assets[BACKGROUND_L] =  pygame.image.load(os.path.join(img_dir, 'lava_1.png')).convert_alpha()
    player_r = pygame.image.load(os.path.join(img_dir, 'wakanda.png')).convert_alpha()
    assets[PLAYER_IMG_R] = pygame.transform.scale(player_r, (PLAYER_WIDTH, PLAYER_HEIGHT))
    player_l = pygame.image.load(os.path.join(img_dir, 'wakanda_l.png')).convert_alpha()
    assets[PLAYER_IMG_L] = pygame.transform.scale(player_l, (PLAYER_WIDTH, PLAYER_HEIGHT))
    enemy = pygame.image.load(os.path.join(img_dir, 'perry.png')).convert_alpha()
    assets[INIMIGO_IMG] = pygame.transform.scale(enemy, (inimigo_width, inimigo_height))
    assets[BLOCK] = pygame.image.load(os.path.join(img_dir, 'tile.png')).convert_alpha()
    assets[VILAO_IMG] = pygame.image.load(os.path.join(img_dir, 'astrotoshi.png')).convert_alpha()
    right_attack_img = pygame.image.load(os.path.join(img_dir, 'right_attack.png')).convert_alpha()
    assets[RIGHT_ATTACK] = pygame.transform.scale(right_attack_img, (ATTACK_WIDTH, ATTACK_HEIGHT))
    left_attack_img = pygame.image.load(os.path.join(img_dir, 'left_attack.png')).convert_alpha()
    assets[LEFT_ATTACK] = pygame.transform.scale(left_attack_img, (ATTACK_WIDTH, ATTACK_HEIGHT))
    toshi_attack_img = pygame.image.load(os.path.join(img_dir, 'dito.png')).convert_alpha()
    assets[TOSHI_ATTACK] = pygame.transform.scale(toshi_attack_img, (T_ATTACK_WIDTH, T_ATTACK_HEIGHT))
    flag_img = pygame.image.load(os.path.join(img_dir, 'flag-end.png')).convert_alpha()
    assets[FLAG] = pygame.transform.scale(flag_img, (FLAG_WIDTH, FLAG_HEIGHT))
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(img_dir, 'PressStart2P.ttf'), 28)
    return assets