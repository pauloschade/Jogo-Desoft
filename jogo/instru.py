import pygame
from os import path
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, BLACK,WHITE, QUIT, GAME


def instru():
    instru = True
    while instru:
        screen = pygame.display.set_mode([HEIGHT, WIDTH])
        screen.fill(BLACK)

        INSTRU = pygame.image.load(path.join(img_dir, 'instru.png')).convert_alpha()
        INSTRU = pygame.transform.scale(INSTRU, (HEIGHT, WIDTH))

        screen.blit(INSTRU,[0, 0])

        now = pygame.time.get_ticks()

        pygame.display.update()
        #while intro:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                instru = False
                state = QUIT
            elif event.type == pygame.KEYUP:
                state = GAME
                instru = False

    return state, now