from os import path

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
VILAO_HEIGHT = int (PLAYER_HEIGHT * 2)

# tamanho de projetil
ATTACK_WIDTH = 40
ATTACK_HEIGHT = 26


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


# Define estados possíveis do jogador
STILL = 0
JUMPING = 1
FALLING = 2
RIGHT = 3
LEFT = 4
