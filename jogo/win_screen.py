import pygame
from os import path
from config import img_dir, snd_dir, BLACK, WHITE, HEIGHT_S, WIDTH_S, QUIT, GAME
from assets import load_assets, SCORE_FONT

def win_screen(bank, times):
    text = ''
    keys_down = {}
    assets = load_assets()
    win = True
    i = 1
    while win:
        screen = pygame.display.set_mode([WIDTH_S, HEIGHT_S])
        screen.fill(BLACK)

        WIN = pygame.image.load(path.join(img_dir, 'winner.png')).convert_alpha()
        WIN = pygame.transform.scale(WIN, (WIDTH_S, HEIGHT_S))
        screen.blit(WIN,[0, 0])
        
        lives = bank[0]
        if lives == 1:
            media = 'C'
        elif lives == 2:
            media = 'B'
        elif lives >= 3:
            media = 'A{}'.format('+' * (lives - 3))

        score = bank[1]

        gametime = times[3] - times[0] - (times[2] - times[1])
        minutes = int(int(gametime / 1000) / 60)
        seconds = (int(gametime / 1000)) - (minutes * 60)
        time = "{}'".format(minutes) + '{}"'.format(seconds)

        final = score + int(3.6 * 1e8 / gametime)

        font = assets[SCORE_FONT]
        name_text = font.render("Gamer name:{}".format(text), True, BLACK)
        screen.blit(name_text, (400, 200))

        score_text = font.render("Score:{}".format(score), True, WHITE)
        time_text = font.render("Time:{}".format(time), True, WHITE)
        final_text = font.render("Final score:{}".format(final), True, WHITE)
        media_text = font.render("Média final:{}".format(media), True, WHITE)
        enter_text = font.render("Digite nome e ENTER", True, WHITE)
        enter_text2 = font.render("Type name and ENTER", True, WHITE)

        screen.blit(score_text,(20, 440))
        screen.blit(time_text,(20, 480))
        screen.blit(final_text,(20, 520))
        screen.blit(media_text,(20, 560))
        screen.blit(media_text,(WIDTH_S-100, 520))
        screen.blit(media_text2,(WIDTH_S-100, 560))

        pygame.display.update()

        # if i == 1:
        #     assets[WIN].play()
        #     i = 0

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                over = False
                return QUIT, score, text
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_BACKSPACE:
                    if len(text)>0:
                        text = text[:-1]
                else:
                    if text == '' and event.key == pygame.K_SPACE:
                        text = ''
                    elif event.key == pygame.K_RETURN:
                        return GAME, final, text
                    elif len(text) <= 10:
                        text += (event.unicode).upper()