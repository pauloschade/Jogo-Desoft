import pygame
from os import path
from config import img_dir, snd_dir, BLACK, WHITE, HEIGHT_S, WIDTH_S, QUIT, GAME
from assets import load_assets, SCORE_FONT
# esse é o arquivo da tela de campeão. a parte do código em que o player digita na tela foi retirada desse site: https://pygame.readthedocs.io/en/latest/4_text/text.html 
def win_screen(bank, times):
    pygame.mixer.music.load(path.join(snd_dir, 'winner.ogg'))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)
    name = ''
    keys_down = {}
    assets = load_assets()
    win = True
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
        name_text = font.render("Gamer name:{}".format(name), True, BLACK)
        screen.blit(name_text, (400, 180))

        score_text = font.render("Score:{}".format(score), True, BLACK)
        time_text = font.render("Time:{}".format(time), True, BLACK)
        final_text = font.render("Final score:{}".format(final), True, BLACK)
        media_text = font.render("Média final:{}".format(media), True, BLACK)
        font2 = pygame.font.Font(path.join(img_dir, 'PressStart2P.ttf'), 20)
        enter_text = font2.render("Digite nome e ENTER", True, BLACK)
        enter_text2 = font2.render("Type name and ENTER", True, BLACK)

        screen.blit(score_text,(20, 440))
        screen.blit(time_text,(20, 480))
        screen.blit(final_text,(20, 520))
        screen.blit(media_text,(20, 560))
        screen.blit(enter_text,(WIDTH_S-400, 520))
        screen.blit(enter_text2,(WIDTH_S-400, 560))

        pygame.display.update()

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                win = False
                return QUIT, score, name
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_BACKSPACE:
                    if len(name)>0:
                        name = name[:-1]
                else:
                    if name == '' and event.key == pygame.K_SPACE:
                        name = ''
                    elif event.key == pygame.K_RETURN and len(name) > 0:
                        return GAME, final, name
                    elif len(name) <= 10:
                        name += (event.unicode).upper()