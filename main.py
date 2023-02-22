import pygame
from game import Game
import os

pygame.init()

# generer la fenetre de notre jeu
pygame.display.set_caption("platformer")
screen = pygame.display.set_mode((1280, 720))

background = pygame.image.load("images/background.jpg")

# charger notre bouton pour lancer la partie
play_button = pygame.image.load("images/play.png")
play_button_rect = play_button.get_rect()
play_button_rect.x, play_button_rect.y = 380, 150

# charger notre jeu
game = Game()

running = True

# variable to keep track of the duration of space key press
space_press_duration = 0

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arriere plan
    screen.blit(background, (0, 0))

    # verifier si notre jeu à commencé ou non
    if game.is_playing:
        # déclencher les instructions de la partie
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenche pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
                game.player.decrease_power()

                # start timing the space key press
                space_press_start_time = pygame.time.get_ticks()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

            # calculate the duration of space key press when it is released
            if event.key == pygame.K_SPACE:
                space_press_end_time = pygame.time.get_ticks()
                space_press_duration = (space_press_end_time - space_press_start_time) / 1000.0
                if space_press_duration>=1:
                    game.player.power = game.player.max_power
                else:
                    game.player.power = space_press_duration * 100
                print(f"Space key pressed for {game.player.power} seconds")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est sur le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode "lancé"
                game.start()

