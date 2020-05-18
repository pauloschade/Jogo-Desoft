import pygame
import os
from config import PLAYER_WIDTH, PLAYER_HEIGHT, img_dir, TILE_SIZE, inimigo_height, inimigo_width, VILAO_HEIGHT, VILAO_WIDHT, ATTACK_HEIGHT, ATTACK_WIDTH

#imagens
BACKGROUND_E = 'background'
PLAYER_IMG_W = 'player_img'
INIMIGO_IMG = 'perry'
VILAO_IMG = "vilao_img"
ATTACK = 'attack'


#tipo de tile
BLOCK = 0
EMPTY = -1
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
    assets[BACKGROUND_E] =  pygame.image.load(os.path.join(img_dir, 'earth_land_em_pe.png')).convert()
    assets[PLAYER_IMG_W] = pygame.image.load(os.path.join(img_dir, 'wakanda.png')).convert_alpha()
    enemy= pygame.image.load(os.path.join(img_dir, 'perry.png')).convert_alpha()
    assets[INIMIGO_IMG] = pygame.transform.scale(enemy, (inimigo_width, inimigo_height))
    assets[BLOCK] = pygame.image.load(os.path.join(img_dir, 'tile.png')).convert_alpha()
    assets[VILAO_IMG] = pygame.image.load(os.path.join(img_dir, 'astrotoshi.png')).convert_alpha()
    attack_img = pygame.image.load(os.path.join(img_dir, 'right_attack.png')).convert_alpha()
    assets[ATTACK] = pygame.transform.scale(attack_img, (ATTACK_WIDTH, ATTACK_HEIGHT))
    return assets