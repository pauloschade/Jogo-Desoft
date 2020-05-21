import random
import pygame
from config import FPS, WIDTH, inimigo_width, inimigo_height, HEIGHT, BLACK, YELLOW, RED, img_dir, PLAYER_WIDTH, PLAYER_HEIGHT, TILE_SIZE, GRAVITY, JUMP_SIZE, SPEED_X, STILL, JUMPING, FALLING, RIGHT, LEFT, VILAO_WIDHT, VILAO_HEIGHT, ATTACK_HEIGHT, ATTACK_WIDTH
from assets import load_assets, BACKGROUND_E, PLAYER_IMG_R, PLAYER_IMG_L, INIMIGO_IMG, VILAO_IMG, RIGHT_ATTACK, LEFT_ATTACK, BLOCK, EMPTY, MAP

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