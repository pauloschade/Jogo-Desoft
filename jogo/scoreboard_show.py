import pygame
import json
from config import FPS, TITULO, WIDTH, HEIGHT, BLACK, YELLOW, RED, BLUE, img_dir, snd_dir, PLAYER_WIDTH, PLAYER_HEIGHT, TILE_SIZE, GRAVITY, JUMP_SIZE, SPEED_X, STILL, JUMPING, FALLING, inimigo_height, inimigo_width, WIDTH_S, HEIGHT_S, QUIT, GAME
from os import path
from assets import load_assets, SCORE_FONT
# esse é o arquivo que calcula e mostra o scoreboard dos 10 melhores jogadores
def scoreboard(score, name):
    assets = load_assets()

    with open ('scoreboard.json', 'r') as arquivo:
        ranking = arquivo.read()
    dicionario = json.loads(ranking)
    dicionario2 = json.loads(ranking)
    for k, v in dicionario2.items():
        if score > v[0]:
            v[0] = score
            v[1] = name
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

    pygame.mixer.music.load(path.join(snd_dir, 'scoreboard.ogg'))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)

    keys_down = {}
    scoreboard = True
    while scoreboard:
        screen = pygame.display.set_mode([WIDTH_S, HEIGHT_S])
        screen.fill(BLACK)

        BACK = pygame.image.load(path.join(img_dir, 'scoreboard.png')).convert_alpha()
        BACK = pygame.transform.scale(BACK, (WIDTH_S, HEIGHT_S))
        screen.blit(BACK,[0, 0])

        font = assets[SCORE_FONT]
        for j, i in dicionario_ranking.items():
            lugar = font.render('{0}º - {1}: {2}'.format(j, i[1], i[0]), True, BLACK)
            screen.blit(lugar, (20, 60 + 40 * int(j)))

        font2 = pygame.font.Font(path.join(img_dir, 'PressStart2P.ttf'), 20)
        next_text = font2.render('restart:TAB quit:SPACE', True, RED)
        screen.blit(next_text, (200, 560))

        font3 = pygame.font.Font(path.join(img_dir, 'PressStart2P.ttf'), 32)
        score_text = font3.render('SCOREBOARD', True, BLUE)
        screen.blit(score_text, (240, 25))

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
        
