import pygame
from os import path
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, BLACK,WHITE, QUIT, GAME


def hist2():
    keys_down = {}
    hist = True
    while hist:
        screen = pygame.display.set_mode([HEIGHT, WIDTH])
        screen.fill(BLACK)

        HIST = pygame.image.load(path.join(img_dir, 'bosstxt.jpg')).convert_alpha()
        HIST = pygame.transform.scale(HIST, (HEIGHT, WIDTH))

        screen.blit(HIST,[0, 0])

        pygame.display.update()
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                hist = False
                state = QUIT
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_TAB:
                    hist = False
                    state = GAME
    
    return state