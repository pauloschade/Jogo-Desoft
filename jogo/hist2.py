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

        font = pygame.font.Font(path.join(img_dir, 'PressStart2P.ttf'), 12)
        tab_text = font.render('Pressione tab', True, (200, 200, 20))
        tab_text2 = font.render('Press tab', True, (200, 200, 20))
        screen.blit(tab_text, (HEIGHT-170, WIDTH-50))
        screen.blit(tab_text2, (HEIGHT-120, WIDTH-30))

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