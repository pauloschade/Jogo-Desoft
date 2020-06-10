import random
import pygame
from config import FPS, WIDTH, inimigo_width, inimigo_height, HEIGHT, BLACK, YELLOW, RED, img_dir, PLAYER_WIDTH, PLAYER_HEIGHT, TILE_SIZE, GRAVITY, JUMP_SIZE, SPEED_X, STILL, JUMPING, FALLING, VILAO_WIDHT, VILAO_HEIGHT, ATTACK_HEIGHT, ATTACK_WIDTH, WIDTH_S, HEIGHT_S 
from assets import load_assets, BACKGROUND_E, PLAYER_IMG_R, PLAYER_IMG_L, INIMIGO_IMG, VILAO_IMG, RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, BLOCK, EMPTY, MAP, TOSHI_ATTACK, FLAG, MAP2, BACKGROUND_L, PLAYER_IMG_S_L, PLAYER_IMG_S_R, PLAYER_IMG_S_L_DOWN, PLAYER_IMG_S_R_DOWN

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

    def attack_right(self):
    # Verifica se pode atirar
        now = pygame.time.get_ticks()
    # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_attack

    # Se já pode atirar novamente...
        if elapsed_ticks > self.attack_ticks:
        # Marca o tick da nova imagem.
            self.last_attack = now
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_attack = Attack_right(self.assets, self.rect.centery, self.rect.right)
            self.groups['all_sprites'].add(new_attack)
            self.groups['all_bullets'].add(new_attack)

    def attack_left(self):
    # Verifica se pode atirar
        now = pygame.time.get_ticks()
    # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_attack

    # Se já pode atirar novamente...
        if elapsed_ticks > self.attack_ticks:
        # Marca o tick da nova imagem.
            self.last_attack = now
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_attack = Attack_left(self.assets, self.rect.centery, self.rect.right)
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
        self.rect.x = column * TILE_SIZE
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

class Attack_right(pygame.sprite.Sprite):
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
        self.rect.x = right - 20

    def update(self):
        # A bala só se move no eixo x
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.right > WIDTH:
            self.kill()

class Attack_left(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets, centery, right):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[LEFT_ATTACK]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centery = centery
        self.speedx = 12  
        self.rect.x = right - 50

    def update(self):
        # A bala só se move no eixo x
        self.rect.x -= self.speedx

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
            self.rect.x = 180
            self.rect.y = 150
            self.speedx = random.randint(-2, 2)
            self.speedy = random.randint(2, 4)

class flag (pygame.sprite.Sprite):
   
    
    def __init__(self, assets):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[FLAG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.speedx = 0
        self.speedy = 0
    def update (self):

        self.rect.x = 100
        self.rect.y = 100
        self.speedx = 0
        self.speedy = 0

class Boss(pygame.sprite.Sprite):

    def __init__(self, vilao_img, assets, groups, row, column, blocks):

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
        self.groups = groups
        self.assets = assets
        # Posiciona o personagem
        # row é o índice da linha embaixo do personagem
        self.rect.centerx = column * TILE_SIZE
        self.rect.y = row * TILE_SIZE
        self.speedx = 0
        self.speedy = 0
        self.lives = 5
        self.last_attack = pygame.time.get_ticks()
        self.attack_ticks = 2000

        self.blocks = blocks
    
    def update(self):

        self.speedy = 0 
        self.speedx += random.randint(-5, 5)
        if self.lives == 4:
            self.speedx = self.speedx * 1.07
            self.attack_ticks = 1750
        elif self.lives == 3:
            self.speedx = self.speedx * 1.15
            self.attack_ticks = 1500
        elif self.lives == 2:
            self.speedx = self.speedx * 1.22
            self.attack_ticks = 1250
        elif self.lives == 1:
            self.speedx = self.speedx * 1.3
            self.attack_ticks = 1000

        # Atualizando a posição do inimigo
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o inimigo bater no final da tela, muda o lado do movimento
        # Tenta andar em x
        self.rect.x += self.speedx
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.right >= WIDTH_S:
            self.rect.right = WIDTH_S - 1
            self.speedx = -1
        elif self.rect.left < 0:
            self.rect.left = 0
            self.speedx = 1

        self.ataque_boss()

    def ataque_boss(self):
    # Verifica se pode atirar
        now = pygame.time.get_ticks()
    # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_attack

    # Se já pode atirar novamente...
        if elapsed_ticks > self.attack_ticks:
        # Marca o tick da nova imagem.
            self.last_attack = now
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_attack = ataque_boss(self.assets, self.rect.centerx, self.rect.y)
            self.groups['all_sprites'].add(new_attack)
            self.groups['all_toshi_attacks'].add(new_attack)

class ataque_boss (pygame.sprite.Sprite):

    def __init__(self, assets, centerx, y):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[TOSHI_ATTACK]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        # Posiciona o personagem
        # row é o índice da linha embaixo do personagem
        self.rect.x = centerx
        self.rect.y = y + 80
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 4)

    def update (self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy
         # Se o ataque passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT_S or self.rect.right < 0 or self.rect.left > WIDTH_S:
            self.kill()

class Player_b(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, player_img, groups, assets, row, column, blocks):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = STILL

        # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
        self.image = player_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Guarda o grupo de blocos para tratar as colisões
        self.blocks = blocks

        # Posiciona o personagem
        # row é o índice da linha embaixo do personagem
        self.rect.y = row * TILE_SIZE
        self.rect.right = (column * TILE_SIZE) + PLAYER_HEIGHT

        self.orientation = 1

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
        self.speedx -= GRAVITY/2 
        # Atualiza o estado para caindo
        if self.speedx * GRAVITY > 0: 
            self.state = FALLING
        # Atualiza a posição x
        self.rect.x += self.speedx

        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedx < 0:
                self.rect.left = collision.rect.right
                # Se colidiu com algo, para de cair
                self.speedx = 0
                # Atualiza o estado para parado
                self.state = STILL
            elif self.speedx > 0:
                self.rect.right = collision.rect.left
                # Se colidiu com algo, para de cair
                self.speedx = 0
                # Atualiza o estado para parado
                self.state = STILL

        # Tenta andar em x
        self.rect.y += self.speedy
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom >= HEIGHT_S:
            self.rect.bottom = HEIGHT_S - 1
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para a direita
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
            # Estava indo para a esquerda
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom

    # Método que faz o personagem pular
    def attack_up(self):
    # Verifica se pode atirar
        now = pygame.time.get_ticks()
    # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_attack

    # Se já pode atirar novamente...
        if elapsed_ticks > self.attack_ticks:
        # Marca o tick da nova imagem.
            self.last_attack = now
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_attack = Attack_up(self.assets, self.rect.centerx, self.rect.top)
            self.groups['all_sprites'].add(new_attack)
            self.groups['all_bullets'].add(new_attack)

    def gravitation(self):
        self.image = pygame.transform.flip(self.image, True, False)
        global GRAVITY
        GRAVITY = - GRAVITY

    def paracima(self):
        if self.orientation == 0:
            self.orientation = 1
            self.image = pygame.transform.flip(self.image, False, True)

    def parabaixo(self):
        if self.orientation == 1:
            self.orientation = 0
            self.image = pygame.transform.flip(self.image, False, True)

class Attack_up(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, assets, centerx, top):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[UP_ATTACK]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.speedy = 60
        self.rect.y = top - 20

    def update(self):
        # A bala só se move no eixo x
        self.rect.y -= self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

class Spawn(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, assets, row, column):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        spawn_img = pygame.transform.scale(tile_img, (SPAWN_SIZE, SPAWN_SIZE))

        # Define a imagem do tile.
        self.image = spawn_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row