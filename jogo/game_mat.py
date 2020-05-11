import pygame

pygame.init()

dimns = (1440, 810)
window = pygame.display.set_mode(dimns)
pygame.display.set_caption('Jogo do Mat')
earth_land = pygame.image.load('assets/img/earth_land.png').convert()
background1 = pygame.transform.scale(earth_land,dimns)

game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            game = False

    window.fill((0, 0, 0))
    window.blit(background1, (0, 0))

    pygame.display.update()

pygame.quit()

