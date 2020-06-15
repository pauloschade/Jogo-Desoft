import pygame
from os import path
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, BLACK,WHITE, INIT, QUIT

pygame.init()


def intro(screen):

    intro = True
    screen = pygame.display.set_mode([HEIGHT, WIDTH])
    screen.fill(BLACK)

    LOGO = pygame.image.load(path.join(img_dir, 'initial.png')).convert_alpha()
    LOGO = pygame.transform.scale(LOGO, (HEIGHT, WIDTH))

    screen.blit(LOGO,[0, 0])

    pygame.display.update()
    while intro:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                intro = False
                state = QUIT
            elif event.type == pygame.KEYUP:
                state = INIT
                intro = False
    return state