import pygame
from os import path
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, BLACK,WHITE, QUIT, GAME


#pygame.init()
#intro()
def instru():
    intro = True
    while intro:
        screen = pygame.display.set_mode([HEIGHT, WIDTH])
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 50)
        setas = font.render("use as setas para mover", True, [245,245,220])
        tiro = font.render("utilize X e Z para atirar", True, [245,245,220])
        instru = font.render("instruções: ", True, [245,245,220])
        screen.blit(setas,(20,100))
        screen.blit(tiro,(20,150))
        screen.blit(instru,(20,50))
        font2 = pygame.font.SysFont(None, 20)
        start = font2.render("pressione qualquer tecla", True, [245,245,220])
        screen.blit(start,(560,370))

        pygame.display.update()
        #while intro:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                intro = False
                state = QUIT

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                state = GAME
                intro = False
    return state
        #