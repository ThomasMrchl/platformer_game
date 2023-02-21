import pygame
import random

#classe qui va gérer la gestion des monstres
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100  #ceci est la vie qu auront les monstres
        self.max_health = 100 #ceci est le nombre de vie maximum du monstre
        self.attack = 0.07
        self.image = pygame.image.load("images/golem.png")
        self.rect = self.image.get_rect()
        self.rect.x = 920 + random.randint(0, 200)
        self.rect.y = 400
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        #infliger les degats
        self.health -= amount


        #verifier si son nouveau nombre de point de vie est inferieur ou egale a 0
        if self.health <= 0:
            #reapparaitre
            self.rect.x = 920 + random.randint(0, 200)
            self.velocity = random.randint(1 ,3)
            self.health = self.max_health

    def update_health_bar(self, surface):
        #dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 100, self.rect.y - 20, self.max_health, 7])
        pygame.draw.rect(surface, (240, 224, 20), [self.rect.x +100, self.rect.y-20, self.health, 7])

    def forward(self):
        #le deplacement ne se fait que si il n'a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le monstre est en collision avec le joueur
        else:
            #infliger des dégats au joueurs
            self.game.player.damage(self.attack)









