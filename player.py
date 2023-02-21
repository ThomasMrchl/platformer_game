import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.power = 0
        self.max_power = 100
        self.attack = 30
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.number_frame = 1
        self.image = pygame.image.load("images/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 400

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le jouer na plus de vie
            self.game.game_over()

    def increase_power(self):
        if self.power < self.max_power:
            self.power += 10

    def update_health_bar(self, surface):
        #dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 20, self.max_health, 7])
        pygame.draw.rect(surface, (17, 242, 48), [self.rect.x , self.rect.y - 20, self.health, 7])

    def update_power_bar(self, surface):
        #dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x, self.rect.y - 30, self.max_power, 7])
        pygame.draw.rect(surface, (255, 0, 0), [self.rect.x, self.rect.y - 30, self.power, 7])

    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))
        self.image = pygame.image.load("images/player.png")

