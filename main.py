import pygame 
from player import Player
import time

name="Thomas"

pygame.display.set_caption("platformer game")
screen = pygame.display.set_mode((1280,720))

#add pygame.NOFRAME for having no borders
background = pygame.image.load("images/pixel_background.jpg")

player = Player(name)

RIGHT_KEY = pygame.K_RIGHT
LEFT_KEY = pygame.K_LEFT
SPACE = pygame.K_SPACE

is_moving = False
running = True

while running: 
    screen.blit(background, (0,0))
    screen.blit(player.image, player.rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == RIGHT_KEY:
                is_moving = True

            elif event.key == LEFT_KEY:
                is_moving = True

            elif event.key == SPACE:
                player.jump()
                
        elif event.type == pygame.KEYUP:
            if event.key == RIGHT_KEY or event.key == LEFT_KEY:
                is_moving = False

    if is_moving:
        if pygame.key.get_pressed()[RIGHT_KEY]:
            player.move_right()
        elif pygame.key.get_pressed()[LEFT_KEY]:
            player.move_left()
