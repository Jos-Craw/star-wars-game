import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, sw_game):
        super().__init__()
        self.screen = sw_game.screen
        self.settings = sw_game.settings
        self.c1 = sw_game.c1
        self.c2 = sw_game.c2
        self.c3 = sw_game.c3
        self.image = (self.c1, self.c2, self.c3)
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = sw_game.xwing.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.image, self.rect)
