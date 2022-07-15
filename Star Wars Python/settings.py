import pygame
import random
import pyganim
import tkinter


class Settings():
    def __init__(self):
        self.p = 0.016
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (0, 0, 0)
        self.bg = pyganim.PygAnimation([('stars/0.gif', self.p), ('stars/1.gif', self.p),
                                        ('stars/2.gif', self.p), ('stars/3.gif', self.p),
                                        ('stars/4.gif', self.p), ('stars/5.gif', self.p),
                                        ('stars/6.gif', self.p), ('stars/7.gif', self.p),
                                        ('stars/8.gif', self.p), ('stars/9.gif', self.p),
                                        ('stars/10.gif', self.p), ('stars/11.gif', self.p),
                                        ('stars/12.gif', self.p), ('stars/13.gif', self.p),
                                        ('stars/14.gif', self.p), ('stars/15.gif', self.p),
                                        ('stars/16.gif', self.p), ('stars/17.gif', self.p),
                                        ('stars/18.gif', self.p), ('stars/19.gif', self.p),
                                        ('stars/20.gif', self.p), ('stars/21.gif', self.p),
                                        ('stars/22.gif', self.p), ('stars/23.gif', self.p),
                                        ('stars/24.gif', self.p), ('stars/25.gif', self.p),
                                        ('stars/26.gif', self.p), ('stars/27.gif', self.p),
                                        ('stars/28.gif', self.p), ('stars/29.gif', self.p),
                                        ('stars/30.gif', self.p), ('stars/31.gif', self.p),
                                        ('stars/32.gif', self.p), ('stars/33.gif', self.p),
                                        ('stars/34.gif', self.p), ('stars/35.gif', self.p),
                                        ('stars/36.gif', self.p), ('stars/37.gif', self.p),
                                        ('stars/38.gif', self.p), ('stars/39.gif', self.p),
                                        ('stars/40.gif', self.p), ('stars/41.gif', self.p),
                                        ('stars/42.gif', self.p), ('stars/43.gif', self.p),
                                        ('stars/44.gif', self.p), ('stars/45.gif', self.p),
                                        ('stars/46.gif', self.p), ('stars/47.gif', self.p),
                                        ('stars/48.gif', self.p), ('stars/49.gif', self.p),
                                        ('stars/50.gif', self.p), ('stars/51.gif', self.p),
                                        ('stars/52.gif', self.p), ('stars/53.gif', self.p),
                                        ('stars/54.gif', self.p), ('stars/55.gif', self.p),
                                        ('stars/56.gif', self.p), ('stars/57.gif', self.p),
                                        ('stars/58.gif', self.p), ('stars/59.gif', self.p),
                                        ('stars/60.gif', self.p), ('stars/61.gif', self.p),
                                        ('stars/62.gif', self.p), ('stars/63.gif', self.p),
                                        ('stars/64.gif', self.p), ('stars/65.gif', self.p),
                                        ('stars/66.gif', self.p), ('stars/67.gif', self.p),
                                        ('stars/68.gif', self.p), ('stars/69.gif', self.p),
                                        ('stars/70.gif', self.p), ('stars/71.gif', self.p),
                                        ('stars/72.gif', self.p), ('stars/73.gif', self.p),
                                        ('stars/74.gif', self.p), ('stars/75.gif', self.p),
                                        ('stars/76.gif', self.p), ('stars/77.gif', self.p),
                                        ('stars/78.gif', self.p), ('stars/79.gif', self.p),
                                        ('stars/80.gif', self.p), ('stars/81.gif', self.p),
                                        ('stars/82.gif', self.p), ('stars/83.gif', self.p),
                                        ('stars/84.gif', self.p), ('stars/85.gif', self.p),
                                        ('stars/86.gif', self.p), ('stars/87.gif', self.p),
                                        ('stars/88.gif', self.p), ('stars/89.gif', self.p),
                                        ('stars/90.gif', self.p), ('stars/91.gif', self.p),
                                        ('stars/92.gif', self.p), ('stars/93.gif', self.p),
                                        ('stars/94.gif', self.p), ('stars/95.gif', self.p),
                                        ('stars/96.gif', self.p), ('stars/97.gif', self.p),
                                        ('stars/98.gif', self.p), ('stars/99.gif', self.p),
                                        ('stars/100.gif', self.p), ('stars/101.gif', self.p),
                                        ('stars/102.gif', self.p), ('stars/103.gif', self.p),
                                        ('stars/104.gif', self.p), ('stars/105.gif', self.p),
                                        ('stars/106.gif', self.p), ('stars/107.gif', self.p),
                                        ('stars/108.gif', self.p), ('stars/109.gif', self.p),
                                        ('stars/110.gif', self.p), ('stars/111.gif', self.p),
                                        ('stars/112.gif', self.p), ('stars/113.gif', self.p),
                                        ('stars/114.gif', self.p), ('stars/115.gif', self.p),
                                        ('stars/116.gif', self.p), ('stars/117.gif', self.p),
                                        ('stars/118.gif', self.p)])
        self.soundfont = pygame.mixer.Sound("sw.wav")
        self.soundlose = pygame.mixer.Sound("march.wav")
        self.soundboom = pygame.mixer.Sound("boom.wav")
        self.soundlaser = pygame.mixer.Sound("laser.wav")
        self.ship_speed = 0.5
        self.tie_speed = 0.2
        self.bullet_speed = 0.8
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullets_allowed = 1
        self.ship_limit = 1
        self.alien_points = 1
