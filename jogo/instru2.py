import pygame
from os import path
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, BLACK,WHITE, QUIT, GAME


def instru2():
    keys_down = {}
    instru = True
    while instru:
        screen = pygame.display.set_mode([HEIGHT, WIDTH])
        screen.fill(BLACK)

        INSTRU = pygame.image.load(path.join(img_dir, 'instru2.png')).convert_alpha()
        INSTRU = pygame.transform.scale(INSTRU, (HEIGHT, WIDTH))

        screen.blit(INSTRU,[0, 0])

        now = pygame.time.get_ticks()

        pygame.display.update()
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                instru = False
                state = QUIT
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_TAB:
                    instru = False
                    state = GAME
    
    return state, now