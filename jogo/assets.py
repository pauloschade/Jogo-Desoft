import pygame
import os
from config import WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, img_dir, snd_dir, TILE_SIZE, inimigo_height, inimigo_width, VILAO_HEIGHT, VILAO_WIDHT, ATTACK_HEIGHT, ATTACK_WIDTH, T_ATTACK_HEIGHT, T_ATTACK_WIDTH, FLAG_WIDTH, FLAG_HEIGHT

#imagens
BACKGROUND_E = 'background'
BACKGROUND_L = "lava"
PLAYER_IMG_R = 'player_img_r'
PLAYER_IMG_L = 'player_img_l'
INIMIGO_IMG = 'perry'
INIMIGO2_IMG = 'bowserjr'
VILAO_IMG = "vilao_img"
RIGHT_ATTACK = 'right_attack'
LEFT_ATTACK = 'left_attack'
UP_ATTACK = 'up_attack'
TOSHI_ATTACK = 'toshi attack'
FLAG = 'flag'
SCORE_FONT = 'score_font'
BACKGROUND_S = "background_space"
PLAYER_IMG_S_R = 'wakanda_space_right'
PLAYER_IMG_S_L = 'wakanda_space_left'
PLAYER_IMG_S_R_DOWN = 'wakanda_space_right_down'
PLAYER_IMG_S_L_DOWN = 'wakanda_space_left_down'
BOSS = 'boss_img'
SPAWN = 'spawn'
PERRY_DEITADO = 'perry_anim'
BOWSERJR_DEITADO = 'bowser_anim'
PERRY_NOISE = 'grrr'
BSRJR_NOISE = 'uaaa'
WAKANDA_FOREVER = "wakanda forever"
FIRE = 'fire'

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
    [BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY],
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


MAP3 = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],

]


def load_assets():
    assets = {}
    assets[BACKGROUND_E] =  pygame.image.load(os.path.join(img_dir, 'earth_land_em_pe.png')).convert_alpha()
    player_r = pygame.image.load(os.path.join(img_dir, 'wakanda.png')).convert_alpha()
    assets[PLAYER_IMG_R] = pygame.transform.scale(player_r, (PLAYER_WIDTH, PLAYER_HEIGHT))
    player_l = pygame.image.load(os.path.join(img_dir, 'wakanda_l.png')).convert_alpha()
    assets[PLAYER_IMG_L] = pygame.transform.scale(player_l, (PLAYER_WIDTH, PLAYER_HEIGHT))
    enemy = pygame.image.load(os.path.join(img_dir, 'perry.png')).convert_alpha()
    assets[INIMIGO_IMG] = pygame.transform.scale(enemy, (inimigo_width, inimigo_height))
    enemy2 = pygame.image.load(os.path.join(img_dir, 'bowserjr.png')).convert_alpha()
    assets[INIMIGO2_IMG] = pygame.transform.scale(enemy2, (inimigo_width, inimigo_height))
    assets[BLOCK] = pygame.image.load(os.path.join(img_dir, 'tile.png')).convert_alpha()
    assets[VILAO_IMG] = pygame.image.load(os.path.join(img_dir, 'astrotoshi.png')).convert_alpha()
    right_attack_img = pygame.image.load(os.path.join(img_dir, 'right_attack.png')).convert_alpha()
    assets[RIGHT_ATTACK] = pygame.transform.scale(right_attack_img, (ATTACK_WIDTH, ATTACK_HEIGHT))
    left_attack_img = pygame.image.load(os.path.join(img_dir, 'left_attack.png')).convert_alpha()
    assets[LEFT_ATTACK] = pygame.transform.scale(left_attack_img, (ATTACK_WIDTH, ATTACK_HEIGHT))
    up_attack_img = pygame.image.load(os.path.join(img_dir, 'up_attack.png')).convert_alpha()
    assets[UP_ATTACK] = pygame.transform.scale(up_attack_img, (ATTACK_HEIGHT, ATTACK_WIDTH))
    toshi_attack_img = pygame.image.load(os.path.join(img_dir, 'dito.png')).convert_alpha()
    assets[TOSHI_ATTACK] = pygame.transform.scale(toshi_attack_img, (T_ATTACK_WIDTH, T_ATTACK_HEIGHT))
    flag_img = pygame.image.load(os.path.join(img_dir, 'flag-end.png')).convert_alpha()
    assets[FLAG] = pygame.transform.scale(flag_img, (FLAG_WIDTH, FLAG_HEIGHT))
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(img_dir, 'PressStart2P.ttf'), 28)
    assets[BACKGROUND_S] =  pygame.image.load(os.path.join(img_dir, 'space.png')).convert_alpha()
    player_space_l =  pygame.image.load(os.path.join(img_dir, 'wakanda_space_l.png')).convert_alpha()
    assets[PLAYER_IMG_S_L] = pygame.transform.scale(player_space_l, (PLAYER_HEIGHT, PLAYER_WIDTH))
    assets[PLAYER_IMG_S_L_DOWN] = pygame.transform.flip(assets[PLAYER_IMG_S_L], False, True)
    player_space_r = pygame.image.load(os.path.join(img_dir, 'wakanda_space.png')).convert_alpha()
    assets[PLAYER_IMG_S_R] = pygame.transform.scale(player_space_r, (PLAYER_HEIGHT, PLAYER_WIDTH))
    assets[PLAYER_IMG_S_R_DOWN] = pygame.transform.flip(assets[PLAYER_IMG_S_R], False, True)
    assets[BOSS] = pygame.image.load(os.path.join(img_dir, 'boss.png')).convert_alpha()
    spawn = pygame.image.load(os.path.join(img_dir, 'spawn.png')).convert_alpha()
    assets[SPAWN] = pygame.transform.scale(spawn, (2 * TILE_SIZE, 2 * TILE_SIZE))

    background_anim = []
    for m in range(8):
        filename = os.path.join(img_dir, 'lava_{}.png'.format(m+1))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (WIDTH, HEIGHT))
        background_anim.append(img)
    assets[BACKGROUND_L] = background_anim

    perry_anim = []
    for i in range(1):
        filename = pygame.image.load(os.path.join(img_dir, 'perry_deitado.png')).convert_alpha()
        img = pygame.transform.scale(filename, (inimigo_height, inimigo_width))
        perry_anim.append(img)
    assets[PERRY_DEITADO] = perry_anim

    bowser_anim = []
    for q in range(1):
        filename1 = pygame.image.load(os.path.join(img_dir, 'bowserjr_deitado.png')).convert_alpha()
        img1 = pygame.transform.scale(filename1, (inimigo_height, inimigo_width))
        bowser_anim.append(img1)
    assets[BOWSERJR_DEITADO] = bowser_anim


    pygame.mixer.music.load(os.path.join(snd_dir, 'game.mp3'))
    pygame.mixer.music.set_volume(0.4)
    assets[PERRY_NOISE] = pygame.mixer.Sound(os.path.join(snd_dir, 'perry_noise.ogg'))
    assets[BSRJR_NOISE] = pygame.mixer.Sound(os.path.join(snd_dir, 'bsrjr_noise.ogg'))
    assets[WAKANDA_FOREVER] = pygame.mixer.Sound(os.path.join(snd_dir, 'wakanda_forever.ogg'))
    assets[FIRE] = pygame.mixer.Sound(os.path.join(snd_dir, 'fire.ogg'))

    return assets