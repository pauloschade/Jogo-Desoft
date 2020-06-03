import pygame
from config import FPS, WIDTH_S, HEIGHT_S, BLACK, YELLOW, RED, img_dir, PLAYER_WIDTH, PLAYER_HEIGHT, TILE_SIZE, GRAVITY, JUMP_SIZE, SPEED_X, STILL, JUMPING, FALLING
from assets import load_assets, BACKGROUND_L, PLAYER_IMG_R, PLAYER_IMG_L, INIMIGO_IMG, VILAO_IMG, RIGHT_ATTACK, LEFT_ATTACK, BLOCK, EMPTY, SCORE_FONT, MAP2, PLAYER_IMG_S_L, PLAYER_IMG_S_R, BACKGROUND_S, MAP3
from sprites import Tile, Player, inimigo, Vilao, Attack_right, Attack_left, ataque_vilao, flag, Boss, ataque_boss
from os import path

def game_screen3(screen, bank2):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    # assets = load_assets(img_dir)
    assets = load_assets()

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    # all_players = pygame.sprite.Group()
    all_inimigos = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group() 
    all_toshi_attacks = pygame.sprite.Group()  
    all_flags = pygame.sprite.Group() 
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador
    blocks = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    # groups['all_players'] = all_players
    groups['all_bullets'] = all_bullets
    groups['all_inimigos'] = all_inimigos
    groups['all_toshi_attacks'] = all_toshi_attacks
    groups['all_flags'] = all_flags

    # Cria Sprite do jogador
    player = Player(assets[PLAYER_IMG_S_R], groups, assets, 16, 1, blocks)

    BACKGROUND_S = pygame.image.load(path.join(img_dir, 'space.png')).convert_alpha()
    BACKGROUND_S = pygame.transform.scale(BACKGROUND_S, (WIDTH_S, HEIGHT_S))

    #cria Vilao
    boss = Boss(assets[VILAO_IMG], assets, groups, 1, 5, blocks)
    all_sprites.add(boss)


    # Cria tiles de acordo com o mapa
    for row in range(len(MAP3)):
        for column in range(len(MAP3[row])):
            tile_type = MAP3[row][column]
            if tile_type == BLOCK:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                blocks.add(tile)

    # Adiciona o jogador no grupo de sprites por último para ser desenhado por
    # cima dos blocos
    # all_players.add(player)
    all_sprites.add(player)

    keys_down = {}
    PLAYING = 0
    DONE = 1
    WIN = 2
    lives = bank2[0]
    score = bank2[1]
    all_hits = 0
    state = PLAYING
    
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
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEED_X
                    player.image = assets[PLAYER_IMG_S_L]
                elif event.key == pygame.K_RIGHT:
                    player.speedx += SPEED_X
                    player.image = assets[PLAYER_IMG_S_R]
                elif event.key == pygame.K_UP:
                    player.jump()
                elif event.key == pygame.K_x:
                    player.attack_right()
                elif event.key == pygame.K_z:
                    player.attack_left()

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_LEFT:
                        player.speedx += SPEED_X
                        player.image = assets[PLAYER_IMG_S_L]
                    elif event.key == pygame.K_RIGHT:
                        player.speedx -= SPEED_X
                        player.image = assets[PLAYER_IMG_S_R]
            

        for i in range (2):
            boss.ataque_boss()

        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        if state == PLAYING:
            # Verifica se houve colisão entre tiro e meteoro
            hits = pygame.sprite.groupcollide(all_inimigos, all_bullets, True, True, pygame.sprite.collide_mask)
            hits2 = pygame.sprite.spritecollide(player, all_inimigos, True, pygame.sprite.collide_mask)
            hits3 = pygame.sprite.spritecollide(player, all_toshi_attacks, True, pygame.sprite.collide_mask)
            hits4 = pygame.sprite.spritecollide(player, all_flags, False, pygame.sprite.collide_mask)
            all_hits = len(hits2) + len(hits3)
            if all_hits > 0:  
                lives -= 1
                score -= 100
                player.kill()
                keys_down = {}
                if lives == 0:
                    state = DONE
                else:
                    state = PLAYING
                    player = Player(assets[PLAYER_IMG_S_R], groups, assets, 16, 1, blocks)
                    all_sprites.add(player)
            if len(hits4) > 0:
                state = WIN
            for inimigoss in hits:
                score += 100
                if score == 800:
                    lives += 1
            for ataquess in hits3:
                ataquess= ataque_vilao(assets)
                all_sprites.add(ataquess)
                all_toshi_attacks.add(ataquess)
            for inimigoss in hits2:
                inimigoss = inimigo(assets[INIMIGO_IMG], 0 , 0, blocks)
                all_sprites.add(inimigoss)
                all_inimigos.add(inimigoss)


        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(BACKGROUND_S, (0,0))
        all_sprites.draw(screen)

        # desenha o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH_S / 2, 10)
        screen.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT_S - 10)
        screen.blit(text_surface, text_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    if state == DONE:
        return 0
    elif state == WIN:
        return 1
