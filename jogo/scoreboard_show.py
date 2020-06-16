import pygame
import json
from config import FPS, TITULO, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, PLAYER_WIDTH, PLAYER_HEIGHT, TILE_SIZE, GRAVITY, JUMP_SIZE, SPEED_X, STILL, JUMPING, FALLING, inimigo_height, inimigo_width, WIDTH_S, HEIGHT_S, QUIT, GAME
from os import path
from assets import load_assets, SCORE_FONT
# esse é o arquivo que calcula e mostra o scoreboard dos 10 melhores jogadores
def scoreboard(score, nome):
    assets = load_assets()

    with open ('scoreboard.json', 'r') as arquivo:
        ranking = arquivo.read()
    dicionario = json.loads(ranking)
    dicionario2 = json.loads(ranking)
    for k, v in dicionario2.items():
        if score > v[0]:
            v[0] = score
            v[1] = nome
            lugar = int(k)
            break
    for i in range(lugar+1, 11):
        dicionario2[str(i)] = dicionario[str(i-1)]
    dicionario = json.dumps(dicionario2)
    with open('scoreboard.json', 'w') as arquivo_json:
        arquivo_json.write(dicionario)
    with open ('scoreboard.json', 'r') as arquivo:
        ranking2 = arquivo.read()
    dicionario_ranking = json.loads(ranking2)

    keys_down = {}
    scoreboard = True
    while scoreboard:
        screen = pygame.display.set_mode([WIDTH_S, HEIGHT_S])
        screen.fill(BLACK)

        font = assets[SCORE_FONT]
        score_text = font.render('SCOREBOARD', True, YELLOW)
        screen.blit(score_text, (WIDTH_S/4, 20))
        for j, i in dicionario_ranking.items():
            lugar = font.render('{0}º - {1}: {2}'.format(j, i[1], i[0]), True, YELLOW)
            screen.blit(lugar, (20, 40 + 40 * int(j)))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scoreboard = False
                return QUIT
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_SPACE:
                    scoreboard = False
                    return QUIT
                elif event.key == pygame.K_TAB:
                    scoreboard = False
                    return GAME
        
