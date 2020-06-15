import pygame
from config import img_dir, snd_dir, BLACK, WHITE, HEIGHT_S, WIDTH_S, QUIT, GAME
from assets import load_assets, SCORE_FONT

def win_screen(bank):
    text = ''
    keys_down = {}
    assets = load_assets()
    win = True
    i = 1
    while win:
        screen = pygame.display.set_mode([WIDTH_S, HEIGHT_S])
        screen.fill(BLACK)

        # WIN = pygame.image.load(path.join(img_dir, 'over.png')).convert_alpha()
        # WIN = pygame.transform.scale(WIN, (HEIGHT_S, WIDTH_S))
        # screen.blit(WIN,[0, 0])
        
        lives = bank[0]
        if lives == 1:
            media = 'C'
        elif lives == 2:
            media = 'B'
        elif lives >= 3:
            media = 'A{}'.format('+' * (lives - 3))

        score = bank[1]

        minutes = int(int(bank[2] / 1000) / 60)
        seconds = (int(bank[2] / 1000)) - (minutes * 60)
        time = "{}'".format(minutes) + '{}"'.format(seconds)

        final = score + int(3,6 * 1e8 / bank[2])

        font = assets[SCORE_FONT]
        score_text = font.render("Score:{}".format(score), True, WHITE)
        screen.blit(score_text,(20, 20))
        time_text = font.render("Time:{}".format(time), True, WHITE)
        screen.blit(time_text,(20, 60))
        final_text = font.render("Final score:{}".format(final), True, WHITE)
        screen.blit(final_text,(20, 100))
        media_text = font.render("Média final:{}".format(media), True, WHITE)
        screen.blit(media_text,(450, 60))

        name_text = font.render("Gamer name:{}".format(text), True, WHITE)

        pygame.display.update()

        # if i == 1:
        #     assets[WIN].play()
        #     i = 0

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                over = False
                return QUIT
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_SPACE:
                    text = ''
                elif event.key == K_BACKSPACE:
                    if len(text)>0:
                        text = text[:-1]
                else:
                    text += (event.unicode).upper()