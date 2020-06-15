import pygame
from os import path
from config import FPS, WIDTH_S, HEIGHT_S, BLACK, YELLOW, RED, img_dir, snd_dir, BLACK,WHITE, QUIT, GAME


def instru2():
    instru2 = True
    while instru2:
        screen = pygame.display.set_mode([HEIGHT_S, WIDTH_S])
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 50)
        setas = font.render("Use as setas dos lados para mudar a gravidade", True, [245,245,220])
        setas2 = font.render("Use as setas de cima/baixo para andar", True, [245,245,220])
        tiro = font.render("Utilize espaço para atirar", True, [245,245,220])
        instru = font.render("instruções: ", True, [245,245,220])
        safe = font.render("você estar seguro dentro do quadrado vermelho ", True, [245,245,220])
        screen.blit(safe, (20, 250))
        screen.blit(setas2, (20, 200))
        screen.blit(setas,(20,100))
        screen.blit(tiro,(20,150))
        screen.blit(instru,(20,50))
        font2 = pygame.font.SysFont(None, 20)
        start = font2.render("Pressione qualquer tecla para iniciar", True, [245,245,220])
        screen.blit(start,(460,370))

        pygame.display.update()
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                instru2 = False
                state = QUIT
            elif event.type == pygame.KEYUP:
                state = GAME
                instru2 = False
    return state