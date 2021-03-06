import pygame
from os import path
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, BLACK,WHITE, QUIT, GAME

# esse é o arquivo da primeira historinha

def hist():
    pygame.mixer.music.load(path.join(snd_dir, 'dark.ogg'))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    keys_down = {}
    hist = True
    while hist:
        screen = pygame.display.set_mode([HEIGHT, WIDTH])
        screen.fill(BLACK)

        HIST = pygame.image.load(path.join(img_dir, 'introtxt.png')).convert_alpha()
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
                    pygame.mixer.music.stop()
                    hist = False
                    state = GAME
    
    return state

