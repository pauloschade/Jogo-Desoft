import pygame
from os import path
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, BLACK,WHITE, QUIT, GAME
from assets import load_assets, GAME_OVER, SCORE_FONT

# esse é o arquivo do game over

def game_over(bank):
    keys_down = {}
    assets = load_assets()
    over = True
    i = 1
    while over:
        screen = pygame.display.set_mode([HEIGHT, WIDTH])
        screen.fill(BLACK)

        OVER = pygame.image.load(path.join(img_dir, 'over.png')).convert_alpha()
        OVER = pygame.transform.scale(OVER, (HEIGHT, WIDTH))

        screen.blit(OVER,[0, 0])

        font = assets[SCORE_FONT]
        score = font.render("Score:{}".format(bank[1]), True, [255,0,0])
        screen.blit(score,(20, 20))

        pygame.display.update()

        if i == 1:
            assets[GAME_OVER].play()
            i = 0

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                over = False
                return QUIT
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_TAB:
                    return GAME