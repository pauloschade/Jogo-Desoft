import pygame
from os import path
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, BLACK,WHITE, INIT2, QUIT

pygame.init()


def intro(screen):

    intro = True
    screen = pygame.display.set_mode([HEIGHT, WIDTH])
    screen.fill(BLACK)

    #logo
    LOGO = pygame.image.load(path.join(img_dir, 'logo.png')).convert_alpha()
    LOGO = pygame.transform.scale(LOGO, (int(WIDTH), int(HEIGHT/3)))

    screen.blit(LOGO,[150, 50])

    font = pygame.font.SysFont(None, 20)
    start = font.render("pressione qualquer tecla", True, [245,245,220])
    screen.blit(start,(560,370))

   


    pygame.display.update()
    while intro:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                intro = False
                state = QUIT
            elif event.type == pygame.KEYUP:
                state = INIT2
                intro = False
    return state
    
#pygame.init()
#intro()


