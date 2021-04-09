import random
import pygame
from config import FPS, WIDTH, inimigo_width, inimigo_height, HEIGHT, BLACK, YELLOW, RED, img_dir, snd_dir, PLAYER_WIDTH, PLAYER_HEIGHT, TILE_SIZE, GRAVITY, JUMP_SIZE, SPEED_X, STILL, VILAO_WIDHT, VILAO_HEIGHT, ATTACK_HEIGHT, ATTACK_WIDTH, WIDTH_S, HEIGHT_S 
from assets import load_assets, BACKGROUND_E, PLAYER_IMG_R, PLAYER_IMG_L, INIMIGO_IMG, VILAO_IMG, RIGHT_ATTACK, LEFT_ATTACK, UP_ATTACK, BLOCK, EMPTY, MAP, TOSHI_ATTACK, FLAG, MAP2, BACKGROUND_L, PLAYER_IMG_S_L, PLAYER_IMG_S_R, PLAYER_IMG_S_L_DOWN, PLAYER_IMG_S_R_DOWN, SPAWN, PERRY_DEITADO, BOWSERJR_DEITADO, FIRE, TOSHI_INJURED

class Interactive(pygame.sprite.Sprite):
    def __init__(self, img, row, column):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = TILE_SIZE * column


class MapElement(Interactive):
    def __init__(self, img, row, column):
        super().__init__(img, row, column)
        self.rect.y = TILE_SIZE * row


class Decoration(MapElement):
    def __init__(self, img, row, column):
        super().__init__(img, row, column)


class Character(Interactive):
    def __init__(self, characterImg, row, column, blocks, initialSpeed):

        super().__init__(characterImg, row, column)
        self.rect.bottom = row * TILE_SIZE
        self.blocks = blocks
        self.speedx = initialSpeed
        self.speedy = 0
        self.correctPosition = initialSpeed
        self.state = STILL
        
    def update(self):
        updateCharacter(self)


class Player(Character):
    def __init__(self, player_img, groups, assets, row, column, blocks):
        super().__init__(player_img, row, column, blocks, 0)
        self.orientation = 'right'
        self.state = STILL
        self.groups = groups
        self.assets = assets
        self.last_attack = pygame.time.get_ticks()
        self.attack_ticks = 1000

    def jump(self):
        if self.state:
            self.speedy -= JUMP_SIZE
            self.state = False
    
    def attack(self, assets, orientation):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_attack
        if elapsed_ticks > self.attack_ticks:
            self.assets[FIRE].play()
            self.last_attack = now
            new_attack = AttackPlayer(self.assets, self.rect.centery, self.rect.right, orientation)
            self.groups['all_sprites'].add(new_attack)
            self.groups['all_bullets'].add(new_attack)
    
    def flag(self):
        self.speedy -= JUMP_SIZE * 1.5 
        self.state = False


class Vilao(Character):
    def __init__(self, vilao_img, row, column, blocks):
        vilao_img = pygame.transform.scale(vilao_img, (VILAO_WIDHT, VILAO_HEIGHT))
        super().__init__(vilao_img, row, column, blocks, 0)
    def flag(self):
        self.speedy -= JUMP_SIZE * 1.5 


class Inimigo(Character):
    def __init__(self, inimigo_img, row, column, blocks):
        super().__init__(inimigo_img, row, column, blocks, 1)
        inimigo_img = pygame.transform.scale(inimigo_img, (inimigo_width, inimigo_height))
        self.rect.y = 0
        self.rect.bottom = row * TILE_SIZE


class AttackPlayer(pygame.sprite.Sprite):
    def __init__(self, assets, centery, right, orientation):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[RIGHT_ATTACK]
        self.rect = self.image.get_rect()
        self.rect.centery = centery
        self.rect.x = right - 20
        self.speedx = 12
        if orientation == "left":
            self.image = assets[LEFT_ATTACK]
            self.rect.x = right - 50
            self.speedx = - self.speedx

    def update(self):
        updateAttackPlayer(self)


class AttackVilao (pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(assets[TOSHI_ATTACK], (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 240
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(1, 3)

    def update (self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = 180
            self.rect.y = 150
            self.speedx = random.randint(-2, 2)
            self.speedy = random.randint(1, 3)


class Boss(Character):
    def __init__(self, vilao_img, assets, groups, row, column, blocks):
        vilao_img = pygame.transform.scale(vilao_img, (VILAO_WIDHT, VILAO_HEIGHT))
        super().__init__(vilao_img, row, column, blocks, 0)
        self.groups = groups
        self.assets = assets
        self.rect.centerx = column * TILE_SIZE
        self.rect.y = row * TILE_SIZE
        self.lives = 5
        self.last_attack = pygame.time.get_ticks()
        self.intervals = [1500, 1000, 900, 800, 500]
        self.attack_ticks = 1500

    def update(self):
        self.speedy = 0 
        self.speedx += random.randint(-2, 2)
        self.attack_ticks = self.intervals[5 - self.lives]
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right >= WIDTH_S:
            self.rect.right = WIDTH_S - 1
            self.speedx = -1
        elif self.rect.left < 0:
            self.rect.left = 0
            self.speedx = 1
        self.attackBoss()

    def attackBoss(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_attack
        if elapsed_ticks > self.attack_ticks:
            self.last_attack = now
            new_attack = AttackBoss(self.assets, self.rect.centerx, self.rect.y)
            self.groups['all_sprites'].add(new_attack)
            self.groups['all_toshi_attacks'].add(new_attack)


class AttackBoss(pygame.sprite.Sprite):
    def __init__(self, assets, centerx, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(assets[TOSHI_ATTACK], (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = centerx
        self.rect.y = y + 80
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(1, 2)

    def update (self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT_S or self.rect.right < 0 or self.rect.left > WIDTH_S:
            self.kill()


class PlayerBoss(pygame.sprite.Sprite):
    def __init__(self, player_img, groups, assets, row, column, blocks):
        pygame.sprite.Sprite.__init__(self)
        self.gravity = 5/2
        self.image = player_img
        self.rect = self.image.get_rect()
        self.blocks = blocks
        self.rect.y = row * TILE_SIZE
        self.rect.right = (column * TILE_SIZE) + PLAYER_HEIGHT
        self.correctPosition = 0
        self.orientation = 1
        self.side = 'left'
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets
        self.last_attack = pygame.time.get_ticks()
        self.attack_ticks = 1000

    def update(self):
        updatePlayerBoss(self)

    def attackUp(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_attack
        if elapsed_ticks > self.attack_ticks:
            self.assets[FIRE].play()
            self.last_attack = now
            if self.rect.y >= 11.5 * TILE_SIZE and self.rect.x <= 3 * TILE_SIZE:
                self.last_attack = now
            else:
                new_attack = AttackUp(self.assets, self.rect.centerx, self.rect.top)
                self.groups['all_sprites'].add(new_attack)
                self.groups['all_bullets'].add(new_attack)

    def gravitation(self):
        self.image = pygame.transform.flip(self.image, True, False)
        self.gravity = - self.gravity

    def paracima(self):
        if self.orientation == 0:
            self.orientation = 1
            self.image = pygame.transform.flip(self.image, False, True)

    def parabaixo(self):
        if self.orientation == 1:
            self.orientation = 0
            self.image = pygame.transform.flip(self.image, False, True)


class AttackUp(pygame.sprite.Sprite):
    def __init__(self, assets, centerx, top):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[UP_ATTACK]
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.speedy = 30
        self.rect.y = top - 20

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom < 0:
            self.kill()


class InimigoMorto(pygame.sprite.Sprite):
    def __init__(self, bottom, x, assets, personagem, ticks):
        pygame.sprite.Sprite.__init__(self)
        self.nome = assets[personagem]
        self.frame = 0 
        self.image = self.nome[self.frame] 
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom 
        self.rect.x = x
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = ticks

    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.nome):
                self.kill()
            else:
                bottom = self.rect.bottom
                x = self.rect.x
                self.image = self.nome[self.frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
                self.rect.x = x


def updateCharacter (objeto):
    objeto.speedy += GRAVITY
    objeto.rect.x += objeto.speedx
    objeto.rect.y += objeto.speedy
    if objeto.speedy > 0:
        objeto.state = False
    objeto.rect.x += objeto.speedx
    inmap(objeto)
    colisao(objeto)

def inmap(objeto):
    if objeto.rect.right >= WIDTH:
        objeto.rect.right = WIDTH - 1
        if objeto.correctPosition == 1:
            objeto.speedx = -1
    elif objeto.rect.left < 0:
        objeto.rect.left = 0
        if objeto.correctPosition == 1:
            objeto.speedx = 1

def colisao(objeto):
    colisaoVertical(objeto)
    colisaoHorizontal(objeto)

def colisaoVertical(objeto):
    collisions = pygame.sprite.spritecollide(objeto, objeto.blocks, False)
    for collision in collisions:
        if objeto.speedy > 0:
            objeto.rect.bottom = collision.rect.top
            objeto.speedy = 0
            objeto.state = STILL
        elif objeto.speedy < 0:
            objeto.rect.top = collision.rect.bottom
            objeto.speedy = 0
            objeto.state = STILL

def colisaoHorizontal(objeto):
    collisions = pygame.sprite.spritecollide(objeto, objeto.blocks, False)
    for collision in collisions:
        if objeto.speedx > 0:
            objeto.rect.right = collision.rect.left
            if objeto.correctPosition != 0:
                objeto.speedx = -objeto.correctPosition
        elif objeto.speedx < 0:
            objeto.rect.left = collision.rect.right
            if objeto.correctPosition != 0:
                objeto.speedx = objeto.correctPosition

def updateAttackPlayer(objeto):
    objeto.rect.x += objeto.speedx
    if objeto.rect.right > WIDTH:
        objeto.kill()

def updatePlayerBoss(objeto):
    objeto.speedx -=  objeto.gravity/2
    objeto.rect.x += objeto.speedx
    collisions = pygame.sprite.spritecollide(objeto, objeto.blocks, False)
    for collision in collisions:
        if objeto.speedx < 0:
            objeto.rect.left = collision.rect.right
            objeto.speedx = 0
        elif objeto.speedx > 0:
            objeto.rect.right = collision.rect.left
            objeto.speedx = 0

    objeto.rect.y += objeto.speedy
    if objeto.rect.top < 0:
        objeto.rect.top = 0
    elif objeto.rect.bottom >= HEIGHT_S:
        objeto.rect.bottom = HEIGHT_S - 1

    collisions = pygame.sprite.spritecollide(objeto, objeto.blocks, False)
    for collision in collisions:
        if objeto.speedy > 0:
            objeto.rect.bottom = collision.rect.top
        elif objeto.speedy < 0:
            objeto.rect.top = collision.rect.bottom