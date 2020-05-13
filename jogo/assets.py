import pygame
import os
from config import PLAYER_WIDTH, PLAYER_HEIGHT, img_dir, TILE_SIZE

#imagens
BACKGROUND_E = 'background'
PLAYER_IMG_W = 'player_img'


#tipo de tile
BLOCK = 0
EMPTY = -1


def load_assets():
    assets = {}
    assets[BACKGROUND_E] =  pygame.image.load(os.path.join(img_dir, 'earth_land_em_pe.png')).convert()
    assets[PLAYER_IMG_W] = pygame.image.load(os.path.join(img_dir, 'wakanda.png')).convert_alpha()
    #faremos um arquivo so para tile?
    assets[BLOCK] = pygame.image.load(os.path.join(img_dir, 'tile.png')).convert()


    return assets