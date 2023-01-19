import pygame

class Player():
    def __init__(self, name):
        self.name = name 
        self.max_health = 100
        self.health = 100
        self.velocity = 5
        self.attack = 30
        self.image = pygame.image.load("images/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 450

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 65, self.rect.y - 20, self.max_health, 7])
        pygame.draw.rect(surface, (17, 242, 48), [self.rect.x + 65, self.rect.y - 20, self.health, 7])

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity