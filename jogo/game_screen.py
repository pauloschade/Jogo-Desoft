import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, BLUE, GREEN, img_dir, snd_dir, PLAYER_WIDTH, PLAYER_HEIGHT, TILE_SIZE, GRAVITY, JUMP_SIZE, SPEED_X, STILL
from assets import load_assets, BACKGROUND_E, PLAYER_IMG_R, PLAYER_IMG_L, INIMIGO_IMG, VILAO_IMG, RIGHT_ATTACK, LEFT_ATTACK, BLOCK, EMPTY, MAP, SCORE_FONT, PERRY_NOISE, WAKANDA_FOREVER, JUMP_NOISE, PERRY_DEITADO, FLAG
from sprites import Decoration, Player, Inimigo, Vilao, AttackPlayer, AttackVilao, InimigoMorto
from os import path

# esse é o arquivo que roda o nível 2 do jogo

def game_screen(screen):

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets()

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    all_inimigos = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group() 
    all_toshi_attacks = pygame.sprite.Group()  
    all_flags = pygame.sprite.Group() 
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador
    blocks = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_bullets'] = all_bullets
    groups['all_inimigos'] = all_inimigos
    groups['all_toshi_attacks'] = all_toshi_attacks
    groups['all_flags'] = all_flags

    # Cria Sprite do jogador
    player = Player(assets[PLAYER_IMG_R], groups, assets, 16, 1, blocks)


    # Criando os inimigos
    for i in range(4):
        inimigoss = Inimigo(assets[INIMIGO_IMG], 4 + 3 * i , -1, blocks)
        all_sprites.add(inimigoss)
        all_inimigos.add(inimigoss)

    BACKGROUND_E = pygame.image.load(path.join(img_dir, 'earth_land_em_pe.png')).convert()
    BACKGROUND_E = pygame.transform.scale(BACKGROUND_E, (WIDTH, HEIGHT))

    #cria Vilao
    vilao = Vilao(assets[VILAO_IMG], 1, 5, blocks)
    all_sprites.add(vilao)

    for i in range(2):
        ataquess= AttackVilao(assets)
        all_sprites.add(ataquess)
        all_toshi_attacks.add(ataquess)
    

    # Cria tiles de acordo com o mapa
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type == BLOCK:
                block = pygame.transform.scale(assets[tile_type], (TILE_SIZE, TILE_SIZE))
                tile = Decoration(block, row, column)
                all_sprites.add(tile)
                blocks.add(tile)

    # Adiciona o jogador no grupo de sprites por último para ser desenhado por
    # cima dos blocos
    all_sprites.add(player)

    # adiciona bandeira
    Flag = Decoration(assets[FLAG], 2.3, 2.5)
    all_sprites.add(Flag)
    all_flags.add(Flag)
    keys_down = {}
    DONE = -1
    OVER = 0
    PLAYING = 1
    WIN = 2
    lives = 3
    score = 0
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
                    player.image = assets[PLAYER_IMG_L]
                    player.orientation = 'left'
                elif event.key == pygame.K_RIGHT:
                    player.speedx += SPEED_X
                    player.image = assets[PLAYER_IMG_R]
                    player.orientation = 'right'
                elif event.key == pygame.K_UP:
                    player.jump()
                elif event.key == pygame.K_SPACE:
                    player.attack(assets, player.orientation)

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key in keys_down and keys_down[event.key]:
                    if event.key == pygame.K_LEFT:
                        player.speedx += SPEED_X
                        player.image = assets[PLAYER_IMG_L]
                    elif event.key == pygame.K_RIGHT:
                        player.speedx -= SPEED_X
                        player.image = assets[PLAYER_IMG_R]

        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        if state == PLAYING:
            hits = pygame.sprite.groupcollide(all_inimigos, all_bullets, False, True, pygame.sprite.collide_mask)
            hits2 = pygame.sprite.spritecollide(player, all_inimigos, True, pygame.sprite.collide_mask)
            hits3 = pygame.sprite.spritecollide(player, all_toshi_attacks, True, pygame.sprite.collide_mask)
            hits4 = pygame.sprite.spritecollide(player, all_flags, False, pygame.sprite.collide_mask)
            all_hits = len(hits2) + len(hits3)
            if all_hits > 0:
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
                    player = Player(assets[PLAYER_IMG_R], groups, assets, 16, 1, blocks)
                    all_sprites.add(player)
            if len(hits4) > 0:
                player.flag()
                vilao.flag()
            if vilao.rect.bottom <= 0:
                state = WIN
            for inimigoss in hits:
                score += 100
                if score == 800:
                    lives += 1
            for ataquess in hits3:
                ataquess= AttackVilao(assets)
                all_sprites.add(ataquess)
                all_toshi_attacks.add(ataquess)
            for inimigoss in hits2:
                inimigoss = Inimigo(assets[INIMIGO_IMG], 0 , 0, blocks)
                all_sprites.add(inimigoss)
                all_inimigos.add(inimigoss)
            for inimigoss in hits:
                # No lugar do perry antigo, adicionar um perry morto.
                assets[PERRY_NOISE].play()
                perry = InimigoMorto(inimigoss.rect.bottom, inimigoss.rect.x, assets, PERRY_DEITADO, 400)
                all_sprites.add(perry)
                inimigoss.kill()

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(BACKGROUND_E, (0,-50))
        all_sprites.draw(screen)

        # desenha o score
        text_surface = assets[SCORE_FONT].render("{:05d}".format(score), True, (255, 128, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2, 10)
        screen.blit(text_surface, text_rect)

        # Desenhando as vidas
        media = assets[SCORE_FONT].render('Média = ', True, BLACK)
        media_rect = media.get_rect()
        media_rect.bottomleft = (10, HEIGHT - 10)
        screen.blit(media, media_rect)
        if lives == 1:
            text_surface = assets[SCORE_FONT].render('C', True, RED)
        elif lives == 2:
            text_surface = assets[SCORE_FONT].render('B', True, YELLOW)
        elif lives >= 3:
            text_surface = assets[SCORE_FONT].render('A{}'.format('+' * (lives - 3)), True, GREEN)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (230, HEIGHT - 10)
        screen.blit(text_surface, text_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    if state == DONE:
        return -1, [lives, score]
    elif state == OVER:
        return 0, [lives, score]
    elif state == WIN:
        assets[JUMP_NOISE].play()
        return 1, [lives, score]
