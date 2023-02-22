from player import Player
from monster import Monster
import pygame
import os


#creer une seconde classe qui va representer notre jeu
class Game:

    def __init__(self):
        #definir si notre jeu a commencé ou non
        self.is_playing = False
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()

    def game_over(self):
        #remettre le jeu à neuf
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False



    def update(self, screen):
        # appliquer l'image de notre joueur
        
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)
        self.player.update_power_bar(screen)

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les montres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # appliquer l'ensemble des images projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groude de méchants
        self.all_monsters.draw(screen)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)