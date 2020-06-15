import pygame
from os import path
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, BLACK,WHITE, QUIT, GAME
from assets import load_assets, GAME_OVER


def game_over(bank):
    assets = load_assets()
    assets[GAME_OVER].play()
    over = True
    while over:
        screen = pygame.display.set_mode([HEIGHT, WIDTH])
        screen.fill(BLACK)

        OVER = pygame.image.load(path.join(img_dir, 'instru.png')).convert_alpha()
        OVER = pygame.transform.scale(OVER, (HEIGHT, WIDTH))

        screen.blit(OVER,[0, 0])

        pygame.display.update()

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                over = False
                state = GAME
            elif event.type == pygame.K_x:
                over = False
                state = QUIT
            elif event.type == pygame.K_z:
                over = False
                state = GAME
    return state