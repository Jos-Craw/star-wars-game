import pygame.font

class Score():
    def __init__(self, sw_game):
        self.screen = sw_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sw_game.settings
        self.stats = sw_game.stats
        self.text_color = (255, 255, 0)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                                          self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)