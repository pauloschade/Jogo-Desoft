import pygame
from os import path
from config import FPS, WIDTH_S, HEIGHT_S, BLACK, YELLOW, RED, img_dir, snd_dir, BLACK,WHITE, QUIT, GAME

# pygame.init()

def scoreboard(score, nome):

    with open ('scoreboard.txt', 'r') as arquivo:
        ranking = arquivo.read()
    lista_ranking = ranking.split(',')
    dicionario_ranking = {}
    i = 0
    while i < len(lista_ranking):
        dicionario_ranking[lista_ranking[i]] = int(lista_ranking[i+1])
        i += 2
    print(dicionario_ranking)
    # a = 9
    # for i in dicionario_ranking.values():
    #     if score >= i:
    #         a -= 1
    #     elif score < i:
    #         break
    lista_valores = []
    lista_nomes = []
    for j, i in dicionario_ranking.items():
        print(i)
        lista_valores.append(i)
        lista_nomes.append(j)
    print(lista_valores)
    lista_valores = lista_valores.sort(reverse=True)
    print(lista_valores)
    for f in lista_valores:
        if score >= f:
            lista_valores.append(score)
            lista_nomes.append(nome)
    lista_valores = lista_valores.sort(reverse=True)
    if len(lista_valores) == 11:
        del(lista_valores[10])
    count = 9
    for c in lista_valores:
        if c == score:
            break
        else:
            count -= 1
    lista_nomes_2 = []
    for co in range(len(lista_nomes)):
        if co < count:
            lista_nomes_2.append(lista_nomes[co])
        elif co == count:
            lista_nomes_2.append(nome)
        else:
            lista_nomes_2.append(lista_nomes[co-1])

    lista_nomes = lista_nome_2

    lista_final = []
    for i in range (lista_nomes):
        lista_final.append(lista_nomes[i])
        lista_final.append(lista_valores[i])

    with open ('scoreboard.txt', 'w') as arquivo:
        arquivo.write(lista_final)

    with open ('scoreboard.txt', 'r') as arquivo:
        conteudo = arquivo.read()

    lista_ranking = conteudo.split(',')
    dicionario_ranking = {}
    i = 0
    while i <= len(lista_ranking):
        dicionario_ranking[lista_ranking[i]] = lista_ranking[i+1]
        i += 2
    scoreboard = True
    while scoreboard:
        a = 0
        for j, i in dicionario_ranking.items():
            a += 1
            screen = pygame.display.set_mode([HEIGHT, WIDTH])
            screen.fill(BLACK)
            font = pygame.Sysfont(None, 50)
            lugar = font.render('{0} - {1}: {2}'.format(a, j, i), True, [245,245,220])
            screen.blit(lugar, (20, 25 + 25 * a))
            pygame.display.update()
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    scoreboard = False
                    state = QUIT
                elif event.type == pygame.KEYUP:
                    state = GAME
                    scoreboard = False
        return state

# scoreboard(2817, 'MAT')
# pygame.quit()
        
