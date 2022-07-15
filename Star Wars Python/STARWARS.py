import sys
import pygame
import random
from settings import Settings
from xwing import Xwing
from tie import TIE
from bolt import Bullet
from game_stats import GameStats
from buttom import Button
from score import Score


class StarWars:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Star Wars Python Edition V.06")
        self.xwing = Xwing(self)
        self.ties = pygame.sprite.Group()
        self.settings.bg.play()
        self.bullets = pygame.sprite.Group()
        self._create_tie()
        self.stats = GameStats(self)
        self.sb = Score(self)
        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.xwing.update()
                self._update_tie()
                self._update_bullets()
            self._update_screen()

    def _create_tie(self):
        tie = TIE(self)
        self.ties.add(tie)

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
        else:
            self.stats.game_active = False

    def _update_tie(self):
        self.ties.update()
        if pygame.sprite.spritecollideany(self.xwing, self.ties):
            self._ship_hit()
            self.settings.soundlose.play()
            self.settings.soundfont.stop()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.xwing.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.xwing.moving_left = True
                elif event.key == pygame.K_UP:
                    self.xwing.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.xwing.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.xwing.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.xwing.moving_left = False
                elif event.key == pygame.K_UP:
                    self.xwing.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.xwing.moving_down = False
                elif event.key == pygame.K_SPACE:
                    self.c1 = random.randint(1, 250)
                    self.c2 = random.randint(1, 250)
                    self.c3 = random.randint(1, 250)
                    self.settings.soundlaser.play()
                    self.fire_bullet()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.ties.empty()
            self.bullets.empty()
            self._create_tie()
            self.settings.soundfont.play()
            self.settings.soundlose.stop()
            self.sb.prep_score()

    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.ties, True, True)
        if collisions:
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()
            self.settings.soundboom.play()
        if not self.ties:
            self.bullets.empty()
            self._create_tie()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.settings.bg.blit(self.screen, (0, 0))
        self.xwing.blitme()
        self.ties.draw(self.screen)
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    sw = StarWars()
    sw.run_game()
