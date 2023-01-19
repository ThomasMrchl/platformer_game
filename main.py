import pygame 

pygame.display.set_caption("platformer game")
screen = pygame.display.set_mode((1280,720))

#add pygame.NOFRAME for having no borders
background = pygame.image.load("images/background.jpg")

running = True

while running: 

    screen.blit(background, (0,0))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
