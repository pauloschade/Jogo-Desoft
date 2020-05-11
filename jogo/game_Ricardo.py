import pygame
import random
from os import path


imagens = path.join(path.dirname(__file__), "assets/img")
pygame.init()

dimns = (1200, 410)
window = pygame.display.set_mode(dimns)
player_HEIGHT = 81
player_WIDTH = 81
font = pygame.font.SysFont(None, 48)
pygame.display.set_caption('Jogo do Mat')
earth_land = pygame.image.load('assets/img/earth_land.png').convert()
background1 = pygame.transform.scale(earth_land,dimns)
player_img = pygame.image.load(path.join(imagens, 'wakanda.png')).convert_alpha()
player_img_small =  pygame.transform.scale(player_img, (player_WIDTH, player_HEIGHT))
player_x = 600
player_y = 270

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            game = False

    window.fill((0, 0, 0))
    window.blit(background1, (0, 0))
    window.blit(player_img_small, (player_x, player_y))

    pygame.display.update()

pygame.quit()


