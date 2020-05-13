import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, img_dir, PLAYER_WIDTH, PLAYER_HEIGHT, TILE_SIZE, GRAVITY, JUMP_SIZE, SPEED_X, STILL, JUMPING, FALLING
from assets import load_assets, PLAYER_IMG_W, BACKGROUND_E, BLOCK, EMPTY, MAP
from sprites import Tile, Player
from os import path

def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    # assets = load_assets(img_dir)
    assets = load_assets()

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador
    blocks = pygame.sprite.Group()

    # Cria Sprite do jogador
    player = Player(assets[PLAYER_IMG_W], 12, 2, blocks)

    BACKGROUND_E = pygame.image.load(path.join(img_dir, 'earth_land_em_pe.png')).convert()
    BACKGROUND_E = pygame.transform.scale(BACKGROUND_E, (WIDTH, HEIGHT))
    

    # Cria tiles de acordo com o mapa
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type == BLOCK:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                blocks.add(tile)

    # Adiciona o jogador no grupo de sprites por último para ser desenhado por
    # cima dos blocos
    all_sprites.add(player)

    PLAYING = 0
    DONE = 1

    state = PLAYING
    while state != DONE:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE

            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx -= SPEED_X

        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(BACKGROUND_E, (0,0))
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
