import pygame

pygame.init()

dimns = (40 * 10, 40 * 18)
window = pygame.display.set_mode(dimns)
pygame.display.set_caption('Jogo do Mat')
earth_land = pygame.image.load('assets/img/earth_land.png').convert()
background1 = pygame.transform.scale(earth_land,(1194, 720))

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP or event.type == pygame.QUIT:
            game = False

    window.fill((0, 0, 0))
    window.blit(background1, (-700, 0))

    pygame.display.update()

pygame.quit()

