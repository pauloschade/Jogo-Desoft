import pygame
from os import path
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, BLACK,WHITE, QUIT, GAME


def hist():
    hist = True
    while hist:
        screen = pygame.display.set_mode([HEIGHT, WIDTH])
        screen.fill(BLACK)

        HIST = pygame.image.load(path.join(img_dir, 'introtxt.jpg')).convert_alpha()
        HIST = pygame.transform.scale(HIST, (HEIGHT, WIDTH))

        screen.blit(HIST,[0, 0])

        pygame.display.update()
        #while intro:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                hist = False
                state = QUIT
            elif event.type == pygame.KEYUP:
                state = GAME
                hist = False
    return state

