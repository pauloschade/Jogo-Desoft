import pygame
from os import path
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, BLACK,WHITE, QUIT, GAME


#pygame.init()
#intro()
def instru():
    instru = True
    while instru:
        screen = pygame.display.set_mode([HEIGHT, WIDTH])
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 50)
        setas = font.render("Use as setas para mover", True, [245,245,220])
        tiro = font.render("Utilize espaço para atirar", True, [245,245,220])
        instru = font.render("instruções: ", True, [245,245,220])
        dica = font.render("dica: cuidado com os temidos", True, [245, 245, 220])
        dica2 = font.render("exercícios do servidor", True, [245, 245, 220])
        screen.blit(dica2, (20, 290))
        screen.blit(dica, (20, 250))
        screen.blit(setas,(20,100))
        screen.blit(tiro,(20,150))
        screen.blit(instru,(20,50))
        font2 = pygame.font.SysFont(None, 20)
        start = font2.render("Pressione qualquer tecla para iniciar", True, [245,245,220])
        screen.blit(start,(460,370))

        pygame.display.update()
        #while intro:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                instru = False
                state = QUIT
            elif event.type == pygame.KEYUP:
                state = GAME
                instru = False
    return state
        #