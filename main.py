import pygame 
from player import Player


name = str(input("Enter your name"))
while name == "":
    name = str(input("Enter your name"))

pygame.display.set_caption("platformer game")
screen = pygame.display.set_mode((1280,720))

#add pygame.NOFRAME for having no borders
background = pygame.image.load("images/background.jpg")

player = Player(name)

running = True

while running: 

    screen.blit(background, (0,0))
    screen.blit(player.image, player.rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
        
