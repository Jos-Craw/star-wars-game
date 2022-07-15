import pygame
from pygame.sprite import Sprite
import random
import time


class TIE(Sprite):
    def __init__(self, sw_game):
        super().__init__()
        self.screen = sw_game.screen
        self.settings = sw_game.settings
        self.screen_rect = sw_game.screen.get_rect()
        self.image = pygame.image.load('tie.ico')
        self.rect = self.image.get_rect()
        self.rect.midtop = self.screen_rect.midtop
        self.settings = sw_game.settings
        self.xt = random.randint(0, 372)
        self.yt = random.randint(0, 372)
        self.x = random.randint(0, 372)
        self.y = random.randint(0, 200)

    def update(self):
        if (self.xt > self.rect.x) and (self.yt == self.rect.y):
            self.x += self.settings.tie_speed
        if (self.xt < self.rect.x) and (self.yt == self.rect.y):
            self.x -= self.settings.tie_speed
        if (self.yt > self.rect.y) and (self.xt == self.rect.x):
            self.y += self.settings.tie_speed
        if (self.yt < self.rect.y) and (self.xt == self.rect.x):
            self.y -= self.settings.tie_speed
        if (self.xt > self.rect.x) and (self.yt > self.rect.y):
            self.x += self.settings.tie_speed
            self.y += self.settings.tie_speed
        if (self.xt < self.rect.x) and (self.yt > self.rect.y):
            self.x -= self.settings.tie_speed
            self.y += self.settings.tie_speed
        if (self.xt < self.rect.x) and (self.yt < self.rect.y):
            self.x -= self.settings.tie_speed
            self.y -= self.settings.tie_speed
        if (self.xt > self.rect.x) and (self.yt < self.rect.y):
            self.x += self.settings.tie_speed
            self.y -= self.settings.tie_speed
        if (self.xt == self.rect.x) and (self.yt == self.rect.y):
            self.xt = random.randint(0, 372)
            self.yt = random.randint(0, 372)
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
