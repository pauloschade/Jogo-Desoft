import pygame
from os import path
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, BLACK,WHITE, QUIT, GAME


def hist2():
    hist2 = True
    while hist2:
        screen = pygame.display.set_mode([HEIGHT, WIDTH])
        screen.fill(BLACK)

        HIST2 = pygame.image.load(path.join(img_dir, 'bosstxt.jpg')).convert_alpha()
        HIST2 = pygame.transform.scale(HIST2, (HEIGHT, WIDTH))

        screen.blit(HIST2,[0, 0])

        pygame.display.update()
        #while intro:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                hist2 = False
                state = QUIT
            elif event.type == pygame.KEYUP:
                state = GAME
                hist2 = False
    return state