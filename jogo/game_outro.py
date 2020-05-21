# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
import random
from os import path
from random import randint


pygame.init()
pygame.mixer.init()


# pasta que contem figuras
img_dir = path.join(path.dirname(__file__), 'assets', 'img')

# Dados gerais do jogo.
TITULO = 'A jornada do oxi'
WIDTH = 400 # Largura da tela
HEIGHT = 720 # Altura da tela 
TILE_SIZE = 40 # Tamanho de cada tile 


#tamanho jogador
PLAYER_WIDTH = TILE_SIZE - 1
PLAYER_HEIGHT = int(TILE_SIZE * 1.5)
FPS = 60 # Frames por segundo


# dados do inimigo
inimigo_width = PLAYER_WIDTH - 5
inimigo_height = PLAYER_HEIGHT

#dados vilao
VILAO_WIDHT = int(PLAYER_WIDTH * 1.5)
VILAO_HEIGHT = int (PLAYER_HEIGHT * 1.5)

# tamanho de projetil
ATTACK_WIDTH = 40
ATTACK_HEIGHT = 26

# ataque do Toshi
T_ATTACK_WIDTH = 40
T_ATTACK_HEIGHT = 26


# algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

# Define a aceleração da gravidade
GRAVITY = 5
# Define a velocidade inicial no pulo
JUMP_SIZE = TILE_SIZE
# Define a velocidade em x
SPEED_X = 5

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load(path.join(img_dir, 'earth_land_em_pe.png')).convert()
BACKGROUND_E = pygame.transform.scale(bg, (WIDTH, HEIGHT))
# Nome do jogo
pygame.display.set_caption(TITULO)

# Imprime instruções
print('*' * len(TITULO))
print(TITULO.upper())
print('*' * len(TITULO))
print('Utilize as setas do teclado para andar e pular.')



# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2
RIGHT = 3
LEFT = 4


#imagens
BACKGROUND_E = 'background'
PLAYER_IMG_R = 'player_img_r'
PLAYER_IMG_L = 'player_img_l'
INIMIGO_IMG = 'perry'
VILAO_IMG = "vilao_img"
RIGHT_ATTACK = 'right_attack'
LEFT_ATTACK = 'left_attack'
TOSHI_ATTACK = 'toshi attack'


#tipo de tile
BLOCK = 0
EMPTY = -1
MAP = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
]



def load_assets():
    assets = {}
    assets[BACKGROUND_E] =  pygame.image.load(path.join(img_dir, 'earth_land_em_pe.png')).convert()
    assets[PLAYER_IMG_R] = pygame.image.load(path.join(img_dir, 'wakanda.png')).convert_alpha()
    assets[PLAYER_IMG_L] = pygame.image.load(path.join(img_dir, 'wakanda_l.png')).convert_alpha()
    enemy= pygame.image.load(path.join(img_dir, 'perry.png')).convert_alpha()
    assets[INIMIGO_IMG] = pygame.transform.scale(enemy, (inimigo_width, inimigo_height))
    assets[BLOCK] = pygame.image.load(path.join(img_dir, 'tile.png')).convert_alpha()
    assets[VILAO_IMG] = pygame.image.load(path.join(img_dir, 'astrotoshi.png')).convert_alpha()
    right_attack_img = pygame.image.load(path.join(img_dir, 'right_attack.png')).convert_alpha()
    assets[RIGHT_ATTACK] = pygame.transform.scale(right_attack_img, (ATTACK_WIDTH, ATTACK_HEIGHT))
    left_attack_img = pygame.image.load(path.join(img_dir, 'left_attack.png')).convert_alpha()
    assets[LEFT_ATTACK] = pygame.transform.scale(left_attack_img, (ATTACK_WIDTH, ATTACK_HEIGHT))
    toshi_attack_img = pygame.image.load(path.join(img_dir, 'dito.png')).convert_alpha()
    assets[TOSHI_ATTACK] = pygame.transform.scale(toshi_attack_img, (T_ATTACK_WIDTH, T_ATTACK_HEIGHT))
    return assets


# Class que representa os blocos do cenário
class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, row, column):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row


# Classe Jogador que representa o herói
class Player(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, player_img, groups, assets, row, column, blocks):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = STILL

        # Ajusta o tamanho da imagem
        player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

        # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
        self.image = player_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Guarda o grupo de blocos para tratar as colisões
        self.blocks = blocks

        # Posiciona o personagem
        # row é o índice da linha embaixo do personagem
        self.rect.x = column * TILE_SIZE
        self.rect.bottom = row * TILE_SIZE

        self.speedx = 0
        self.speedy = 0

        self.groups = groups
        self.assets = assets


        self.last_attack = pygame.time.get_ticks()
        self.attack_ticks = 1000


    # Metodo que atualiza a posição do personagem
    def update(self):
        # Vamos tratar os movimentos de maneira independente.
        # Primeiro tentamos andar no eixo y e depois no x.

        # Tenta andar em y
        # Atualiza a velocidade aplicando a aceleração da gravidade
        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        # Atualiza a posição y
        self.rect.y += self.speedy
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
        if self.speedx > 0:
            self.state = RIGHT
        elif self.speedx < 0:
            self.state = LEFT

        # Tenta andar em x
        self.rect.x += self.speedx
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right

    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
    def attack(self):
    # Verifica se pode atirar
        now = pygame.time.get_ticks()
    # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_attack

    # Se já pode atirar novamente...
        if elapsed_ticks > self.attack_ticks:
        # Marca o tick da nova imagem.
            self.last_attack = now
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_attack = Attack(self.assets, self.rect.centery, self.rect.right)
            self.groups['all_sprites'].add(new_attack)
            self.groups['all_bullets'].add(new_attack)


# Classe inimigo
class inimigo(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, inimigo_img, row, column, blocks):

        # Construtor da classe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = inimigo_img
        # ajusta o tamanho do inimigo
        inimigo_img = pygame.transform.scale(inimigo_img, (inimigo_width, inimigo_height))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.rect.bottom =  row * TILE_SIZE
        self.speedx = 1
        self.speedy = 0
        # Guarda o grupo de blocos para tratar as colisões
        self.blocks = blocks
    def update (self):

        self.speedy += GRAVITY

        # Atualizando a posição do inimigo
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o inimigo bater no final da tela, muda o lado do movimento
        # Tenta andar em x
        self.rect.x += self.speedx
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1
            self.speedx = -1
        elif self.rect.left < 0:
            self.rect.left = 0
            self.speedx = 1


        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions_ini = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions_ini:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0

         # Se colidiu com algum bloco, volta para o ponto antes da colisão e muda de sentido
        collisions_ini = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions_ini:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
                self.speedx = -1
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right
                self.speedx = 1



class Attack(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets, centery, right):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[RIGHT_ATTACK]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centery = centery
        self.speedx = 12  
        self.rect.x = right - 10

    def update(self):
        # A bala só se move no eixo x
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.right > WIDTH:
            self.kill()






class Vilao(pygame.sprite.Sprite):

    def __init__(self, vilao_img, row, column, blocks):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = STILL

        # Ajusta o tamanho da imagem
        vilao_img = pygame.transform.scale(vilao_img, (VILAO_WIDHT, VILAO_HEIGHT))

        # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
        self.image = vilao_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o personagem
        # row é o índice da linha embaixo do personagem
        self.rect.centerx = column * TILE_SIZE
        self.rect.y = row * TILE_SIZE
        self.speedx = 0
        self.speedy = 0

        self.blocks = blocks

    def update (self):

        self.speedy += GRAVITY

        # Atualizando a posição do inimigo
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o inimigo bater no final da tela, muda o lado do movimento
        # Tenta andar em x
        self.rect.x += self.speedx
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1
            self.speedx = -1
        elif self.rect.left < 0:
            self.rect.left = 0
            self.speedx = 0


        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions_ini = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions_ini:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0

         # Se colidiu com algum bloco, volta para o ponto antes da colisão e muda de sentido
        collisions_ini = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions_ini:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
                self.speedx = -1
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right
                self.speedx = 1

class ataque_vilao (pygame.sprite.Sprite):

    def __init__(self, assets):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[TOSHI_ATTACK]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        # Posiciona o personagem
        # row é o índice da linha embaixo do personagem
        self.rect.x = 200
        self.rect.y = 240
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 4)

    def update (self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy
         # Se o ataque passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = 200
            self.rect.y = 240
            self.speedx = random.randint(-2, 2)
            self.speedy = random.randint(2, 4)


def game_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    # assets = load_assets(img_dir)
    assets = load_assets()

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    all_inimigos = pygame.sprite.Group()
    all_bullets = pygame.sprite.Group()
    all_toshi_attacks = pygame.sprite.Group()  
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador
    blocks = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_bullets'] = all_bullets
    groups['all_inimigos'] = all_inimigos
    groups['all_toshi_attacks'] = all_toshi_attacks

    # Cria Sprite do jogador
    player = Player(assets[PLAYER_IMG_R], groups, assets, 16, 1, blocks)
    if player.state == LEFT:
        player = Player(assets[PLAYER_IMG_L], groups, assets, 16, 1, blocks)

    # Criando os inimigos
    for i in range(4):
        inimigoss = inimigo(assets[INIMIGO_IMG], 4 + 3 * i , -1, blocks)
        all_sprites.add(inimigoss)
        all_inimigos.add(inimigoss)

    BACKGROUND_E = pygame.image.load(path.join(img_dir, 'earth_land_em_pe.png')).convert()
    BACKGROUND_E = pygame.transform.scale(BACKGROUND_E, (WIDTH, HEIGHT))

    #cria Vilao
    vilao = Vilao(assets[VILAO_IMG], 1, 5, blocks)
    all_sprites.add(vilao)

    for i in range(2):
        ataquess= ataque_vilao(assets)
        all_sprites.add(ataquess)
        all_toshi_attacks.add(ataquess)


    

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
                elif event.key == pygame.K_UP:
                    player.jump()
                elif event.key == pygame.K_SPACE:
                    player.attack()

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

        if state == PLAYING:
            # Verifica se houve colisão entre tiro e meteoro
            hits = pygame.sprite.groupcollide(all_inimigos, all_bullets, True, True, pygame.sprite.collide_mask)
            #for inimigoss in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
                # O meteoro e destruido e precisa ser recriado
                #inimigoss = inimigo(assets[INIMIGO_IMG], 0, 0, blocks)
                #all_sprites.add(inimigoss)
                #all_inimigos.add(inimigoss)

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(BACKGROUND_E, (0,-50))
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()



# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()
