import pygame
from config import FPS, WIDTH_S, HEIGHT_S, BLACK, YELLOW, RED, BLUE, GREEN, img_dir, snd_dir, PLAYER_WIDTH, PLAYER_HEIGHT, TILE_SIZE, GRAVITY, JUMP_SIZE, SPEED_X, STILL, JUMPING, FALLING, SPEED_Y
from sprites import Tile, Player, Player_b, inimigo, Vilao, Attack_right, Attack_left, ataque_vilao, flag, Boss, ataque_boss, Spawn, Toshi_machucado
from assets import load_assets, BACKGROUND_L, PLAYER_IMG_R, PLAYER_IMG_L, INIMIGO_IMG, VILAO_IMG, RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, BLOCK, EMPTY, SCORE_FONT, MAP2, PLAYER_IMG_S_L, PLAYER_IMG_S_R, BACKGROUND_S, MAP3, BOSS, SPAWN, WAKANDA_FOREVER, BOSS_NOISE
from os import path

def game_screen3(screen, bank):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    # assets = load_assets(img_dir)
    assets = load_assets()

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group() 
    all_toshi_attacks = pygame.sprite.Group()
    blocks = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    # groups['all_players'] = all_players
    groups['all_bullets'] = all_bullets
    groups['all_toshi_attacks'] = all_toshi_attacks
    #groups["all_spawn"] = all_spawn


    # Cria Sprite do jogador
    player = Player_b(assets[PLAYER_IMG_S_L], groups, assets, 13, 1, blocks)

    BACKGROUND_S = pygame.image.load(path.join(img_dir, 'space.png')).convert_alpha()
    BACKGROUND_S = pygame.transform.scale(BACKGROUND_S, (WIDTH_S, HEIGHT_S))

    #cria Vilao
    boss = Boss(assets[BOSS], assets, groups, 1, WIDTH_S/2, blocks)
    all_sprites.add(boss)

    #imagem spawn
    spawn = Spawn(assets[SPAWN], 12, 1)
    #all_spawn.add(spawn)
    all_sprites.add(spawn)

    # Cria tiles de acordo com o mapa
    for row in range(len(MAP3)):
        for column in range(len(MAP3[row])):
            tile_type = MAP3[row][column]
            if tile_type == BLOCK:
                tile = Tile(pygame.image.load(path.join(img_dir, 'tile_space.png')).convert_alpha(), row, column)
                all_sprites.add(tile)
                blocks.add(tile)
    
    global GRAVITY

    # Adiciona o jogador no grupo de sprites por último para ser desenhado por
    # cima dos blocos
    # all_players.add(player)
    all_sprites.add(player)

    keys_down = {}
    DONE = -1
    OVER = 0
    PLAYING = 1
    WIN = 2
    lives = bank[0] + 1
    score = bank[1]
    state = PLAYING

    pygame.mixer.music.load(path.join(snd_dir, 'boss.mp3'))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops=-1)

    while state == PLAYING:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE

            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_UP:
                    player.paracima()
                    player.speedy -= 5
                elif event.key == pygame.K_DOWN:
                    player.parabaixo()
                    player.speedy += 5
                elif event.key == pygame.K_RIGHT:
                    if player.side == 'left':
                        player.gravitation()
                        player.side = 'right'
                elif event.key == pygame.K_LEFT:
                    if player.side == 'right':
                        player.gravitation()
                        player.side = 'left'
                elif event.key == pygame.K_SPACE:
                    player.attack_up()

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_UP:
                        player.speedy += 5
                    elif event.key == pygame.K_DOWN:
                        player.speedy -= 5
            

        # for i in range (2):
        #     boss.ataque_boss()

        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        if state == PLAYING:
            # Verifica se houve colisão entre tiro e meteoro
            hits3 = pygame.sprite.spritecollide(player, all_toshi_attacks, True, pygame.sprite.collide_mask)
            hits4 = pygame.sprite.spritecollide(boss, all_bullets, True, pygame.sprite.collide_mask)
            hits5 = pygame.sprite.spritecollide(spawn, all_bullets, True, pygame.sprite.collide_mask)
            hits6 = pygame.sprite.spritecollide(spawn, all_toshi_attacks, True, pygame.sprite.collide_mask)
            if len(hits3) > 0:
                assets[WAKANDA_FOREVER].play()   
                lives -= 1
                score -= 100
                player.kill()
                keys_down = {}
                if lives == 0:
                    pygame.mixer.music.stop()
                    state = OVER
                else:
                    state = PLAYING
                    #if GRAVITY < 0:
                        #GRAVITY = - GRAVITY
                    player = Player_b(assets[PLAYER_IMG_S_L], groups, assets, 13, 1, blocks)
                    all_sprites.add(player)
            for ataquess in hits3:
                ataquess= ataque_vilao(assets)
                all_sprites.add(ataquess)
                all_toshi_attacks.add(ataquess)
            if len(hits4) > 0:
                assets[BOSS_NOISE].play()
                score += 100
                boss.lives -= 1
                boss_injured = Toshi_machucado(boss.rect.bottom, boss.rect.x, assets)
                all_sprites.add(boss_injured)
                if boss.lives == 0:
                    state = WIN
                    boss.kill()

        now = pygame.time.get_ticks()

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(BACKGROUND_S, (0,0))
        all_sprites.draw(screen)

        # desenha o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, BLUE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH_S / 2, 10)
        screen.blit(text_surface, text_rect)

        # Desenhando as vidas
        media = assets[SCORE_FONT].render('Média = ', True, BLACK)
        media_rect = media.get_rect()
        media_rect.bottomleft = (10, HEIGHT_S - 10)
        screen.blit(media, media_rect)
        if lives == 1:
            text_surface = assets[SCORE_FONT].render('C', True, RED)
        if lives == 2:
            text_surface = assets[SCORE_FONT].render('B', True, YELLOW)
        if lives >= 3:
            text_surface = assets[SCORE_FONT].render('A{}'.format('+' * (lives - 3)), True, GREEN)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (230, HEIGHT_S - 10)
        screen.blit(text_surface, text_rect)

        patience = assets[SCORE_FONT].render("Toshi's patience = ", True, BLACK)
        patience_rect = patience.get_rect()
        patience_rect.bottomleft = (WIDTH_S - 690, HEIGHT_S - 10)
        screen.blit(patience, patience_rect)
        if boss.lives == 1:
            text2_surface = assets[SCORE_FONT].render('0.01%', True, (192, 0, 64))
        elif boss.lives == 2:
            text2_surface = assets[SCORE_FONT].render('1%', True, RED)
        elif boss.lives == 3:
            text2_surface = assets[SCORE_FONT].render('10%', True, (255, 128, 0))
        elif boss.lives == 4:
            text2_surface = assets[SCORE_FONT].render('25%', True, YELLOW)
        elif boss.lives == 5:
            text2_surface = assets[SCORE_FONT].render('50%', True, GREEN)
        text2_rect = text2_surface.get_rect()
        text2_rect.bottomleft = (WIDTH_S - 150, HEIGHT_S - 10)
        screen.blit(text2_surface, text2_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    if state == DONE:
        return -1, [lives, score], now
    elif state == OVER:
        return 0, [lives, score], now
    elif state == WIN:
        return 1, [lives, score], now
