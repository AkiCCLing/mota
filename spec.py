import pygame

class Upstair(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.type = "upstair"
        self.image=pygame.image.load('images/upstair.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        screen.blit(self.image, self.rect)

class Downstair(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.type = "downstair"
        self.image=pygame.image.load('images/downstair.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        screen.blit(self.image, self.rect)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.type = "terrain"
        self.image=pygame.image.load('images/wall.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y

    def draw(self, screen, index):
        screen.blit(self.image, self.rect)
